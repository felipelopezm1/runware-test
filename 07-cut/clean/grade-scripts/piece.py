"""Render one piece: video frames [va,vb) of vsrc, audio [aa,ab) of asrc at 48 kHz stereo.
Audio: ffmpeg loudnorm two-pass to -14 LUFS / -1.5 dBTP (linear when it can be), then, when the short
piece lands more than 0.2 LU off, a residual gain trim with a -1.5 dB limiter, measured again (up to 4 times).
Silent pieces are left silent. Video H.264 CRF 14 high, bt709 tv, 24 fps."""
import sys, json, subprocess, re, os
c = json.loads(sys.argv[1]); fps = 24
va, vb, aa, ab = c['va'], c['vb'], c['aa'], c['ab']; N = vb - va; dur = N / fps
wav = c['out'] + '.tmp.wav'; wav2 = c['out'] + '.tmp2.wav'
def run(args): return subprocess.run(args, capture_output=True, text=True)
def meas(path):
    r = run(['ffmpeg','-hide_banner','-i',path,'-af','ebur128=peak=true','-f','null','-'])
    I = re.findall(r'I:\s+(-?[\d.]+) LUFS', r.stderr); TP = re.findall(r'Peak:\s+(-?[\d.inf]+) dBFS', r.stderr)
    return float(I[-1]), TP[-1]
abase = f"atrim=start={aa/fps}:end={ab/fps},asetpts=PTS-STARTPTS,aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo"
info = {'out': c['out'], 'frames': N, 'dur': round(dur, 4)}
if c.get('norm', True):
    r = run(['ffmpeg','-hide_banner','-i',c['asrc'],'-af',abase+",loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json",'-f','null','-'])
    m = json.loads(re.findall(r'\{[^{}]*"input_i"[^{}]*\}', r.stderr)[-1]); info['in_I'] = m['input_i']; info['in_TP'] = m['input_tp']
    ln = (f",loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}"
          f":measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true:print_format=json,aresample=48000")
    r = run(["ffmpeg","-hide_banner","-y","-i",c["asrc"],"-af",abase+",apad=pad_dur=1"+ln+f",asetpts=N/SR/TB,apad,atrim=end={dur}",'-c:a','pcm_f32le',wav])
    info['loudnorm_mode'] = (re.findall(r'"normalization_type"\s*:\s*"(\w+)"', r.stderr) or ['?'])[-1]
    I, TP = meas(wav); info['after_loudnorm_I'] = I; trims = []
    for _ in range(4):
        if abs(I + 14) <= 0.2: break
        g = -14 - I; trims.append(round(g, 2))
        run(['ffmpeg','-hide_banner','-y','-i',wav,'-af',f"volume={g}dB,alimiter=limit=-1.5dB:attack=5:release=60:level=disabled:latency=1",'-c:a','pcm_f32le',wav2])
        os.replace(wav2, wav); I, TP = meas(wav)
    info['trims_dB'] = trims
else:
    run(['ffmpeg','-hide_banner','-y','-i',c['asrc'],'-af',abase+f",apad,atrim=end={dur}",'-c:a','pcm_f32le',wav]); info['silent'] = True
vf = f"trim=start_frame={va}:end_frame={vb},setpts=PTS-STARTPTS,format=yuv420p"
r = run(['ffmpeg','-hide_banner','-y','-i',c['vsrc'],'-i',wav,'-map','0:v','-map','1:a','-vf',vf,
         '-c:v','libx264','-preset','slow','-crf','14','-profile:v','high','-level','4.1','-pix_fmt','yuv420p','-r','24','-g','48',
         '-color_primaries','bt709','-color_trc','bt709','-colorspace','bt709','-color_range','tv',
         '-c:a','aac','-b:a','256k','-ar','48000','-ac','2','-t',str(dur),'-movflags','+faststart', c['out']])
if r.returncode: print(r.stderr[-2000:]); sys.exit(1)
os.remove(wav)
info['out_I'], info['out_TP'] = meas(c['out'])
p = json.loads(run(['ffprobe','-v','error','-show_entries','stream=codec_type,nb_frames,duration','-of','json',c['out']]).stdout)['streams']
info['streams'] = {s['codec_type']: [s.get('nb_frames'), s.get('duration')] for s in p}
print(json.dumps(info))

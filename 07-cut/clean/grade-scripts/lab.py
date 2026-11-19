import numpy as np
M=np.array([[0.4124564,0.3575761,0.1804375],[0.2126729,0.7151522,0.0721750],[0.0193339,0.1191920,0.9503041]])
Mi=np.linalg.inv(M); WP=np.array([0.95047,1.0,1.08883])
def s2l(c): return np.where(c<=0.04045,c/12.92,((c+0.055)/1.055)**2.4)
def l2s(c): c=np.clip(c,0,1); return np.where(c<=0.0031308,c*12.92,1.055*np.power(c,1/2.4)-0.055)
def f(t): d=6/29; return np.where(t>d**3,np.cbrt(t),t/(3*d*d)+4/29)
def fi(t): d=6/29; return np.where(t>d,t**3,3*d*d*(t-4/29))
def rgb2lab(rgb):
    xyz=s2l(rgb)@M.T/WP; fx,fy,fz=f(xyz[...,0]),f(xyz[...,1]),f(xyz[...,2])
    return np.stack([116*fy-16,500*(fx-fy),200*(fy-fz)],-1)
def lab2rgb(lab):
    fy=(lab[...,0]+16)/116; fx=fy+lab[...,1]/500; fz=fy-lab[...,2]/200
    xyz=np.stack([fi(fx),fi(fy),fi(fz)],-1)*WP
    return l2s(xyz@Mi.T)

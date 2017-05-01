import matplotlib.pyplot as plt

N = 8
a = np.random.rand(N)

b = np.fft.rfft(a)
d = np.append(b,np.conj(((b[1:])[:-1])[::-1]))

e = np.zeros(N)*1j
f = np.zeros(N)*1j

for i in range(N):
    f[i] = d[0] + d[N/2]*np.exp(2j*np.pi*i/2)
    for j in range(1,N/2):
        f[i] += 2*np.real(d[j])*np.cos(2*np.pi*i/N*j) - 2*np.imag(d[j])*np.sin(2*np.pi*i/N*j)
    f[i] /= N
    
print np.linalg.norm(a-f)
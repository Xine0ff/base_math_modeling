from lec_3_module import earth_mass as em
from lec_3_module import sigma_stelf_bolc as G
from lec_3_module import gravity_constant as sigma

g=500*G/(10**2)
print(g)

x=em*G*sigma
print(x)
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = alt * larg
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(larg,alt,area))
tinta = area / 2
print('Para píntar essa parede, você precisará de {}l de tinta'.format(tinta))
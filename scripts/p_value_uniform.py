# Скрипт для расчета теоретического и наблюдаемого p-value.
# Теоретическое p-value рассчитывается из экспоненциального распределения,
# наблюдаемое генерируется из гамма-распределения. При shape=1,
# гамма-распределение совпадает с экспоненциальным, поэтому для shape=1 должна
# получиться диагональ. В остальных случаях, кривая должна отклоняться от
# диагонали.

from typing import List, Tuple
import matplotlib.pyplot as plt
import numpy as np

plt.xkcd()
plt.gcf().subplots_adjust(bottom=0.15)


def sampling(shape: float = 1, size=1000) -> np.array:
    generator = np.random.default_rng()
    return generator.gamma(shape, size=size)


def exponent_p_value(x: float) -> float:
    if x < 0:
        return 0
    return np.exp(-x)


def theoretical_observed_p_value(shape: float,
                                 size: int = 1000
                                 ) -> Tuple[List[float], List[float]]:
    X = sampling(shape, size)
    xs, ys = [], []
    for x in range(10):
        p_value = exponent_p_value(x)
        p_value_observed = np.sum(X > x) / size
        xs.append(p_value)
        ys.append(p_value_observed)
    return xs, ys


xs, ys = theoretical_observed_p_value(1)
plt.plot(xs, ys, '--', label='k=1')

xs, ys = theoretical_observed_p_value(2.71)
plt.plot(xs, ys, '-*', color='#bcbcbc', label='k=2.71')

xs, ys = theoretical_observed_p_value(0.7)
plt.plot(xs, ys, '-o', color='#bcbcbc', label='k=0.7')


plt.xlabel('theoretical p-value')
plt.ylabel('observed p-value')
plt.legend()

# plt.savefig('theoretical_observed_p_value.pdf', pad_inches=3.5)
plt.show()

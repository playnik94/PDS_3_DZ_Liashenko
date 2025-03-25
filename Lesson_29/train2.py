from PDF import extract_pdf
from  scipy.stats import chi2

xf = extract_pdf()


Xi = [156, 160, 164, 168, 172, 176, 180, 184]
Ni = [8, 14, 20, 32, 12, 8, 4, 2]


class ExamStat:
    X = []
    D = []
    G = []
    Zi_1 = []
    laplaceTable = []

    def __init__(self, xi, ni, n):
        self.xi = xi
        self.ni = ni
        self.n = n

    # X! = 1/n * (Xi * ni)
    # D! = 1/n * (Xi**2 * ni) - X!**2
    # G! = D**0.5

    def means(self):
        for x, n in zip(self.xi, self.ni):
            ExamStat.X.append(x * n)

        ExamStat.X = sum(ExamStat.X)
        ExamStat.X = 1 / self.n * ExamStat.X

        for x, n in zip(self.xi, self.ni):
            ExamStat.D.append(x**2 * n)

        ExamStat.D = sum(ExamStat.D)
        ExamStat.D = (1 / self.n) * ExamStat.D - ExamStat.X**2

        ExamStat.G = float(ExamStat.D**0.5)
        ExamStat.X = float(ExamStat.X)
        self.xi = [x+2 for x in self.xi]

        return print(f'Expected value: {ExamStat.X}  dispersion: {round(ExamStat.D, 3)} MSE: {ExamStat.G}')

        # intervals
        # Zi-1 = ai - 1 - x! / G
        #  Zi  = ai - x! / G
        #  ni! = n * pi
        #  pi  = fi(Zi-1) - fi(Zi)
        # K_емп = (ni - ni!)**2 / ni!
        # K_емп = sum((ni - ni!)**2 / ni!)

    def intervals(self):

        ExamStat.Zi_1 = [round(abs(j), 2) for j in ExamStat.Zi_1]

        for x in self.xi:
            ExamStat.Zi_1.append(abs(round((x - ExamStat.X) / ExamStat.G, 2)))

        zi_1_zi = []

        for i in ExamStat.Zi_1:
            if i not in xf:
                i = i - 0.01
            zi_1_zi.append(round(i, 3))

        zi_1 = []
        zi = []

        for i in zi_1_zi:
            zi_1.append(xf.get(i))
            zi.append(xf.get(i))
        zi_1.insert(0, 0.5)
        zi[-1] = 0.5

        pi = []
        n_i = []
        ni_ni2 = []
        n = 100
        k_emp = []

        for a, b, c, nI in zip(zi_1_zi, zi_1, zi, self.ni):
            pi.append(round(abs(b - c), 4))
            n_i.append(round(n * round(abs(b - c), 4)))

        for a, b, c, p, j, k in zip(zi_1_zi, zi_1, zi, pi, self.ni, n_i):
            ni_ni2.append(round((j - k)**2 / k, 3))

            print(f'{a} : {b} : {c} : {p} : {round((j - k)**2 / k, 3)}')

        print('')
        m = len(self.ni)
        s = 2  # Параметры
        r = m - s - 1 # Спетень свободы
        a = 0.01 # уровень значимости для использования

        k_kr = chi2.ppf(1-a, df=r)
        k_emp = sum(ni_ni2)**0.5

        if k_kr > k_emp:
            print(f'К-крт > К-емп {k_kr , k_emp}: Гипотеза H0 принимается ')
        else:
            print(f'К-крт < К-емп {k_kr, k_emp}: Гипотеза H1 принимается ')


T = ExamStat(Xi, Ni, sum(Ni))
T.means()
T.intervals()




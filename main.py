def enter_connectivity_matrix ():
    matrix = []
    n = int(input("Ведите количество вершин графа:"))
    print("Введите матрицу смежности:")
    for  i in range(n):
        matrix.append([int(x) for x in input().split()])
    return matrix

def get_multipliers(matrix):
    mtpls = [];
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                mtpls.append([i+1,j+1])
    return mtpls

def get_dnf(matrix):

    mtpls = get_multipliers(matrix);
    dnf = [];
    n = len(mtpls)
    for i in range (2**n):
        el = set();
        k = i
        for j in range(len(mtpls)):
            el.add(mtpls[j][k%2])
            k//=2
        not_subset = True
        if el not in dnf:
            for elem in dnf:
                if el <= elem:
                    dnf.remove(elem)
                if elem <= el:
                    not_subset = False

            if not_subset: dnf.append(el)
    return dnf

def get_ans(matrix):
    ans = "Максимальные внутренне устойчивые подмножества графа:\n"
    dnf = get_dnf(matrix)
    n = len(matrix)
    k = 0
    for el in dnf:
        a = [x+1 for x in range(n)]
        for _ in range (len(el)):
            a.remove(el.pop())
        k+=1
        ans +=  str(k) + ') ' + '{ '
        for e in a: ans += 'V' + str(e) +  ' '
        ans+='}\n'
    return ans

if __name__ == "__main__" :
    matrix = enter_connectivity_matrix()
    print(get_ans(matrix))
def knapsack_brute(W, wt, val, n):
    """
    Mencari nilai maksimal yang dapat dimasukkan ke dalam knapsack.
    W = beban maksimal knapsack
    wt = list berat masing-masing barang
    val = list nilai masing-masing barang
    n = jumlah barang yang tersedia (panjang list)
    """

    # Base case: jika tidak ada barang tersisa
    #            atau beban tampung maksimal 0

    if n == 0 or W == 0:
        return [0, []]

    elif wt[n-1] > W:
        return knapsack_brute(W, wt, val, n-1)

    # Kembalikan salah satu dengan nilai max dari dua kasus berikut:
    # 1) item ke-N termasuk
    # 2) item ke-N tidak termasuk

    simpan1 = knapsack_brute(W-wt[n-1], wt, val, n-1)
    simpan2 = knapsack_brute(W, wt, val, n-1)

    nilai1 = val[n-1] + simpan1[0]
    nilai2 = simpan2[0]

    nilai_max =  max(
        nilai1,
        nilai2
    )

    if nilai_max == nilai1:
        simpan1[0] = nilai_max
        index_item = [n-1]
        simpan1[1].extend(index_item)
        return simpan1
    else:
        return simpan2

if __name__ == "__main__":
    val = [200, 60, 100, 120]
    wt = [30, 10, 20, 15]
    item_name = ["pensil", "pulpen", "buku", "penghapus"]
    W = 50
    n = len(val)

    hasil = knapsack_brute(W, wt, val, n)
    for i in hasil[1]:
        print(item_name[i])


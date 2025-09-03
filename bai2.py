import math
# ==============================
# HÀM GIẢI TSP BẰNG NHÁNH - CẬN
# ==============================
CHI_PHI_TOI_THIEU_HIEN_TAI = math.inf
DUONG_DI_TOT_NHAT_HIEN_TAI = []

def giai_tsp_bnbl_don_gian(GRAPH_TSP, current_city, current_path, current_cost):
    """
    Giải bài toán TSP bằng nhánh cận đơn giản
    GRAPH_TSP   : ma trận chi phí
    current_city: thành phố hiện tại
    current_path: các thành phố đã đi
    current_cost: chi phí hiện tại
    """
    global CHI_PHI_TOI_THIEU_HIEN_TAI, DUONG_DI_TOT_NHAT_HIEN_TAI

    SO_THANH_PHO = len(GRAPH_TSP)

    # --- Cắt tỉa (Pruning) ---
    if current_cost >= CHI_PHI_TOI_THIEU_HIEN_TAI:
        print(f"CẮT NHÁNH: {current_path} (cost={current_cost}) ≥ {CHI_PHI_TOI_THIEU_HIEN_TAI}")
        return

    # --- Điều kiện dừng (đã thăm hết thành phố) ---
    if len(current_path) == SO_THANH_PHO:
        cost_to_return = GRAPH_TSP[current_city][current_path[0]]
        if cost_to_return != math.inf:
            tong_chi_phi = current_cost + cost_to_return
            if tong_chi_phi < CHI_PHI_TOI_THIEU_HIEN_TAI:
                CHI_PHI_TOI_THIEU_HIEN_TAI = tong_chi_phi
                DUONG_DI_TOT_NHAT_HIEN_TAI = current_path + [current_path[0]]
                print(f"==> TÌM THẤY ĐƯỜNG MỚI: {DUONG_DI_TOT_NHAT_HIEN_TAI} cost={tong_chi_phi}")
        return

    # --- Nhánh (Branching) ---
    for next_city in range(SO_THANH_PHO):
        if next_city not in current_path and GRAPH_TSP[current_city][next_city] != math.inf:
            giai_tsp_bnbl_don_gian(
                GRAPH_TSP,
                next_city,
                current_path + [next_city],
                current_cost + GRAPH_TSP[current_city][next_city]
            )

def run_case(GRAPH_TSP):
    global CHI_PHI_TOI_THIEU_HIEN_TAI, DUONG_DI_TOT_NHAT_HIEN_TAI
    CHI_PHI_TOI_THIEU_HIEN_TAI = math.inf
    DUONG_DI_TOT_NHAT_HIEN_TAI = []

    print("\n--- GIẢI BÀI TOÁN NGƯỜI DU LỊCH (TSP) ---")
    print("Ma trận chi phí:")
    for row in GRAPH_TSP:
        print(row)

    # Chạy thuật toán bắt đầu từ TP0
    giai_tsp_bnbl_don_gian(GRAPH_TSP, 0, [0], 0)

    if CHI_PHI_TOI_THIEU_HIEN_TAI == math.inf:
        print("\n [red] Không tìm được đường đi hợp lệ (đồ thị không đầy đủ). [/red]")
    else:
        print(f"\nTổng chi phí đường đi ngắn nhất: {CHI_PHI_TOI_THIEU_HIEN_TAI}")
        print(f"Đường đi tối ưu: {DUONG_DI_TOT_NHAT_HIEN_TAI}")
# Ví dụ 3 thành phố
GRAPH_TSP_3 = [
    [math.inf, 20, 30],
    [20, math.inf, 15],
    [30, 15, math.inf]
]
# Ví dụ 5 thành phố
GRAPH_TSP_5 = [
    [math.inf, 10, 8, 9, 7],
    [10, math.inf, 10, 5, 6],
    [8, 10, math.inf, 8, 9],
    [9, 5, 8, math.inf, 6],
    [7, 6, 9, 6, math.inf]
]
# Ví dụ có đường bị chặn
GRAPH_TSP_BLOCK = [
    [math.inf, 20, math.inf],
    [20, math.inf, 15],
    [math.inf, 15, math.inf]
]
# Chạy thử
run_case(GRAPH_TSP_3)
run_case(GRAPH_TSP_5)
run_case(GRAPH_TSP_BLOCK)
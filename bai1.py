# ----------------- BÀI TOÁN CÁI TÚI 0/1 - NHÁNH CẬN ĐƠN GIẢN -----------------

# Thay đổi dữ liệu theo yêu cầu (có thể thử nhiều bộ khác nhau)
VAT_PHAM = [(2, 3), (3, 4), (4, 8), (5, 8), (9, 10)]
SUC_CHUA_TOI_DA = 10  # Sức chứa tối đa của túi

# Biến toàn cục để lưu trữ giá trị tốt nhất tìm được và lựa chọn tương ứng
GIA_TRI_TOI_DA_HIEN_TAI = 0
LUA_CHON_TOT_NHAT_HIEN_TAI = []

# Biến toàn cục để đếm số lần hàm được gọi (theo dõi số nhánh đã xét)
SO_LAN_GOI_HAM = 0

def giai_knapsack_bnbl_don_gian(idx, current_weight, current_value, current_selection):
    """
    Hàm giải bài toán cái túi 0/1 bằng ý tưởng Nhánh cận đơn giản.
    idx: Chỉ số của vật phẩm đang xét (bắt đầu từ 0).
    current_weight: Trọng lượng hiện tại của các vật phẩm đã chọn.
    current_value: Tổng giá trị hiện tại của các vật phẩm đã chọn.
    current_selection: Danh sách các vật phẩm đã chọn cho đến nay.
    """
    global GIA_TRI_TOI_DA_HIEN_TAI, LUA_CHON_TOT_NHAT_HIEN_TAI, SO_LAN_GOI_HAM

    # Đếm số lần gọi hàm
    SO_LAN_GOI_HAM += 1

    # --- Cắt tỉa (Pruning) ---
    # Nếu trọng lượng hiện tại đã vượt quá sức chứa của túi, nhánh này không hợp lệ
    if current_weight > SUC_CHUA_TOI_DA:
        return

    # Nếu giá trị hiện tại tốt hơn kỷ lục trước đó, cập nhật kết quả
    if current_value > GIA_TRI_TOI_DA_HIEN_TAI:
        GIA_TRI_TOI_DA_HIEN_TAI = current_value
        LUA_CHON_TOT_NHAT_HIEN_TAI = list(current_selection)  # copy danh sách

    # Nếu đã xét hết tất cả vật phẩm, dừng nhánh này
    if idx == len(VAT_PHAM):
        return

    # --- Nhánh (Branching) ---
    item_weight, item_value = VAT_PHAM[idx]

    # 1. NHÁNH: CHỌN vật phẩm hiện tại (nếu không vượt sức chứa)
    if current_weight + item_weight <= SUC_CHUA_TOI_DA:
        giai_knapsack_bnbl_don_gian(
            idx + 1,
            current_weight + item_weight,
            current_value + item_value,
            current_selection + [VAT_PHAM[idx]]
        )

    # 2. NHÁNH: KHÔNG CHỌN vật phẩm hiện tại
    giai_knapsack_bnbl_don_gian(
        idx + 1,
        current_weight,
        current_value,
        current_selection
    )

# ----------------- CHẠY CHƯƠNG TRÌNH -----------------
print("--- Giải Bài toán cái túi bằng Nhánh cận (đơn giản) ---")
giai_knapsack_bnbl_don_gian(0, 0, 0, [])

print(f"Sức chứa túi tối đa: {SUC_CHUA_TOI_DA}")
print(f"Các vật phẩm có sẵn (trọng lượng, giá trị): {VAT_PHAM}")
print(f"Tổng giá trị lớn nhất có thể đạt được: {GIA_TRI_TOI_DA_HIEN_TAI}")
print(f"Các vật phẩm được chọn: {LUA_CHON_TOT_NHAT_HIEN_TAI}")
print(f"Số lần hàm được gọi (số nhánh đã xét): {SO_LAN_GOI_HAM}")

# ----------------- GIẢI THÍCH -----------------
"""
- Thay đổi SUC_CHUA_TOI_DA và VAT_PHAM → kết quả tối ưu thay đổi tương ứng.
- GIA_TRI_TOI_DA_HIEN_TAI lưu giá trị tốt nhất hiện tại, giúp bỏ qua (cắt tỉa) các nhánh không cần thiết.
- SO_LAN_GOI_HAM cho ta biết chương trình đã duyệt bao nhiêu nhánh.
  Khi túi nhỏ hoặc vật phẩm nặng → ít nhánh được xét (do cắt tỉa nhiều).
  Khi túi lớn và vật phẩm nhẹ → nhiều nhánh được xét (gần 2^n).
"""

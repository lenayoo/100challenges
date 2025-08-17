from PIL import Image

# PNG → JPG 변환 함수
def png_to_jpg(png_path, jpg_path, quality=95):
    # PNG 열기
    img = Image.open(png_path).convert("RGB")  # JPG는 투명도 지원 안 하므로 RGB 변환 필요
    # JPG로 저장
    img.save(jpg_path, "JPEG", quality=quality)

# JPG → PNG 변환 함수
def jpg_to_png(jpg_path, png_path):
    # JPG 열기
    img = Image.open(jpg_path)
    # PNG로 저장
    img.save(png_path, "PNG")

# 사용 예시
# png_to_jpg("./4.PNG", "output.jpg")
jpg_to_png("./output.jpg", "rollback.png")
print("변환 완료!")

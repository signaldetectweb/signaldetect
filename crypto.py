import base64
import os

# JSON 파일이 저장된 디렉토리 경로 (현재 디렉토리로 설정)
directory = "."

# 1. 파일 처리 범위 설정
for i in range(1, 31):
    file_name = f"{i}.json"
    file_path = os.path.join(directory, file_name)

    # 2. 파일 존재 여부 확인
    if os.path.exists(file_path):
        # 3. JSON 파일 읽기
        with open(file_path, "r", encoding="utf-8") as f:
            json_data = f.read()

        # 4. Base64로 변환
        base64_encoded_data = base64.b64encode(json_data.encode("utf-8")).decode("utf-8")

        # 5. Base64 데이터를 같은 파일에 저장
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(base64_encoded_data)

        print(f"{file_name} 파일이 성공적으로 인코딩되어 저장되었습니다.")
    else:
        print(f"{file_name} 파일이 존재하지 않습니다.")

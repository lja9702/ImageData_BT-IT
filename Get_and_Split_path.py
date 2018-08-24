import os

FILE_PATH = '/JinahsGit/ImageData_BT-IT/dataSets/Coat/12_245000.jpg'   ###경로 수정하기

#======================================================================================================
#가져온 path에서 디렉토리와 파일명 분리 추출

#WINDOW는 이것도 해줘야 됌
# 드라이브명까지 포함된 Windows 전용 패스를 취급
#split_path = os.path.splitdrive(FILE_PATH)

# 드라이브 이름 (MS윈도우의 경우)
#drive_name = split_path[0]  # D:
#------------------------------------------------------------------------------------------------------

split_path = os.path.split(FILE_PATH) ##윈도우는 FILE_PATH대신 split_path[1]를 사용

# 디렉토리명 구하기
dir_path = split_path[0]

# 패스에서 파일명만 구하기 (확장자 포함)
filename_includeExt = split_path[1]

filename2 = os.path.splitext(FILE_PATH)

#패스에서 파일명만 구하기 (확장자 제외)
filename_noExt = (os.path.split(filename2[0]))[1]

# 확장자만 구하기
get_extention = filename2[1]
#======================================================================================================

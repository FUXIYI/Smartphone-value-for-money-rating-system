# ==================== 1. SoC 打分 ====================
# 分数越高越好，85分=顶级旗舰，1分=入门级
SOC_SCORES = [
    {"分数": 85, "型号": "骁龙 8 Elite Gen 5"},
    {"分数": 84, "型号": "天玑 9500"},
    {"分数": 83, "型号": "Apple A19 Pro"},
    {"分数": 82, "型号": "骁龙 8 Elite"},
    {"分数": 81, "型号": "Apple A19"},
    {"分数": 80, "型号": "天玑 9500s"},
    {"分数": 79, "型号": "天玑 9400+"},
    {"分数": 78, "型号": "天玑 9400"},
    {"分数": 77, "型号": "小米玄戒 O1"},
    {"分数": 76, "型号": "骁龙 8 Gen 5"},
    {"分数": 75, "型号": "Apple A18 Pro"},
    {"分数": 74, "型号": "Apple A18"},
    {"分数": 73, "型号": "天玑 8550"},
    {"分数": 72, "型号": "天玑 9300+"},
    {"分数": 71, "型号": "骁龙 8 Gen 3"},
    {"分数": 70, "型号": "天玑 9300"},
    {"分数": 69, "型号": "骁龙 8s Gen 4"},
    {"分数": 68, "型号": "天玑 9400e"},
    {"分数": 67, "型号": "Apple A17 Pro"},
    {"分数": 66, "型号": "天玑 8500"},
    {"分数": 65, "型号": "天玑 8450"},
    {"分数": 64, "型号": "麒麟 9030 Pro"},
    {"分数": 63, "型号": "Apple A16"},
    {"分数": 62, "型号": "天玑 8400"},
    {"分数": 61, "型号": "骁龙 8 Gen 2"},
    {"分数": 60, "型号": "天玑 9200+"},
    {"分数": 59, "型号": "麒麟 9020"},
    {"分数": 58, "型号": "骁龙 8s Gen 3"},
    {"分数": 57, "型号": "骁龙 7+ Gen 3"},
    {"分数": 56, "型号": "天玑 9200"},
    {"分数": 55, "型号": "Apple A15 (5核)"},
    {"分数": 54, "型号": "天玑 8350"},
    {"分数": 53, "型号": "麒麟 9030S"},
    {"分数": 52, "型号": "骁龙 8+ Gen 1"},
    {"分数": 51, "型号": "天玑 8300"},
    {"分数": 50, "型号": "麒麟 9010"},
    {"分数": 49, "型号": "Apple A14"},
    {"分数": 48, "型号": "骁龙 8 Gen 1"},
    {"分数": 47, "型号": "天玑 9000+"},
    {"分数": 46, "型号": "骁龙 7+ Gen 2"},
    {"分数": 45, "型号": "麒麟 9000S"},
    {"分数": 44, "型号": "天玑 8200"},
    {"分数": 43, "型号": "Apple A13"},
    {"分数": 42, "型号": "天玑 8100"},
    {"分数": 41, "型号": "骁龙 888+"},
    {"分数": 40, "型号": "麒麟 9000"},
    {"分数": 39, "型号": "骁龙 870"},
    {"分数": 38, "型号": "天玑 8050"},
    {"分数": 37, "型号": "麒麟 8020"},
    {"分数": 36, "型号": "骁龙 7 Gen 3"},
    {"分数": 35, "型号": "天玑 7400X"},
    {"分数": 34, "型号": "天玑 7350"},
    {"分数": 33, "型号": "骁龙 778G+"},
    {"分数": 32, "型号": "天玑 7200 Ultra"},
    {"分数": 31, "型号": "骁龙 6 Gen 2"},
    {"分数": 30, "型号": "天玑 7300"},
    {"分数": 29, "型号": "麒麟 8000"},
    {"分数": 28, "型号": "骁龙 780G"},
    {"分数": 27, "型号": "天玑 1200"},
    {"分数": 26, "型号": "骁龙 4 Gen 2"},
    {"分数": 25, "型号": "天玑 7050"},
    {"分数": 24, "型号": "骁龙 695"},
    {"分数": 23, "型号": "天玑 6300"},
    {"分数": 22, "型号": "骁龙 4 Gen 1"},
    {"分数": 21, "型号": "天玑 920"},
    {"分数": 20, "型号": "骁龙 765G"},
    {"分数": 19, "型号": "天玑 1080"},
    {"分数": 18, "型号": "麒麟 990 5G"},
    {"分数": 17, "型号": "骁龙 865+"},
    {"分数": 16, "型号": "天玑 820"},
    {"分数": 15, "型号": "天玑 810"},
    {"分数": 14, "型号": "骁龙 750G"},
    {"分数": 13, "型号": "天玑 700"},
    {"分数": 12, "型号": "骁龙 855+"},
    {"分数": 11, "型号": "骁龙 730G"},
    {"分数": 10, "型号": "天玑 6100+"},
    {"分数": 9, "型号": "骁龙 480+"},
    {"分数": 8, "型号": "麒麟 985"},
    {"分数": 7, "型号": "天玑 6020"},
    {"分数": 6, "型号": "骁龙 712"},
    {"分数": 5, "型号": "麒麟 820"},
    {"分数": 4, "型号": "骁龙 675"},
    {"分数": 3, "型号": "天玑 800U"},
    {"分数": 2, "型号": "骁龙 845"},
    {"分数": 1, "型号": "麒麟 980"},
]

# ==================== 2. 存储系统 ====================

# 2.1 运行内存 (RAM) - LPDDR版本打分
RAM_TYPES = [
    {"版本": "LPDDR6", "分数": 8},
    {"版本": "1γ LPDDR5X", "分数": 7},
    {"版本": "LPDDR5X Ultra Pro", "分数": 6},
    {"版本": "LPDDR5T", "分数": 5},
    {"版本": "LPDDR5X Ultra", "分数": 4},
    {"版本": "LPDDR5X（标准）", "分数": 3},
    {"版本": "LPDDR5", "分数": 2},
    {"版本": "LPDDR4X", "分数": 1},
]

# 2.1.1 运行内存容量档位（RAM 容量）
RAM_CAPACITY_TIERS = [
    {"容量_GB": 4,  "分数": 1},
    {"容量_GB": 6,  "分数": 2},
    {"容量_GB": 8,  "分数": 3},
    {"容量_GB": 12, "分数": 4},
    {"容量_GB": 16, "分数": 5},
    {"容量_GB": 20, "分数": 6},
    {"容量_GB": 24, "分数": 7},
    {"容量_GB": 32, "分数": 8},
    {"容量_GB": 48, "分数": 9},
]
# 2.2 机身存储 (ROM) - 存储版本打分
ROM_TYPES = [
    {"类型": "UFS", "版本": "UFS 5.0", "分数": 14},
    {"类型": "UFS", "版本": "UFS 4.1", "分数": 13},
    {"类型": "UFS", "版本": "UFS 4.0", "分数": 12},
    {"类型": "NVMe", "版本": "Apple A19 Pro (iPhone 17 Pro)", "分数": 11},
    {"类型": "NVMe", "版本": "Apple A18 Pro (iPhone 16 Pro)", "分数": 10},
    {"类型": "UFS", "版本": "UFS 3.1", "分数": 9},
    {"类型": "NVMe", "版本": "Apple A18 (iPhone 16)", "分数": 8},
    {"类型": "NVMe", "版本": "Apple A17 Pro (iPhone 15 Pro)", "分数": 7},
    {"类型": "NVMe", "版本": "Apple A16 (iPhone 14 Pro/15)", "分数": 6},
    {"类型": "NVMe", "版本": "Apple A15 (iPhone 13 Pro/14)", "分数": 5},
    {"类型": "UFS", "版本": "UFS 3.0", "分数": 4},
    {"类型": "NVMe", "版本": "Apple A14 (iPhone 12/13)", "分数": 3},
    {"类型": "UFS", "版本": "UFS 2.2", "分数": 2},
    {"类型": "NVMe", "版本": "Apple A13 (iPhone 11)", "分数": 1},
]

# 2.3 存储容量档位打分
CAPACITY_TIERS = [
    {"容量_GB": 64, "分数": 1},
    {"容量_GB": 128, "分数": 2},
    {"容量_GB": 256, "分数": 3},
    {"容量_GB": 512, "分数": 4},
    {"容量_GB": 1024, "分数": 5},
    {"容量_GB": 2048, "分数": 6},
]

# 2.4 扩展内存打分（TF卡容量档位）
# 说明：华为NM卡 > MicroSD（TF卡），NM卡额外+1分
EXPAND_STORAGE = [
    {"容量_GB": 64, "分数": 1},
    {"容量_GB": 128, "分数": 2},
    {"容量_GB": 256, "分数": 3},
    {"容量_GB": 512, "分数": 4},
    {"容量_GB": 1024, "分数": 5},
    {"容量_GB": 2048, "分数": 6},
]
NM_CARD_BONUS = 1  # 华为NM卡比TF卡额外+1分

# ==================== 3. 显示系统 ====================

# 3.1 显示面板类型（修复：使用字典带分数，按优劣排序）
PANEL_TYPES = [
    {"类型": "双层OLED", "分数": 4},
    {"类型": "单层OLED", "分数": 3},
    {"类型": "AMOLED", "分数": 2},
    {"类型": "LCD", "分数": 1},
]

# 3.2 分辨率打分
RESOLUTIONS = [
    {"分数": 1, "分辨率": "HD / 720P"},
    {"分数": 2, "分辨率": "HD+"},
    {"分数": 3, "分辨率": "FHD / 1080P"},
    {"分数": 4, "分辨率": "FHD+"},
    {"分数": 5, "分辨率": "1.5K"},
    {"分数": 6, "分辨率": "QHD / 2K"},
    {"分数": 7, "分辨率": "QHD+ / 2K+"},
    {"分数": 8, "分辨率": "UHD / 4K"},
]

# 3.3 刷新率打分
REFRESH_RATES = [
    {"分数": 1, "刷新率": "60Hz"},
    {"分数": 2, "刷新率": "75Hz"},
    {"分数": 3, "刷新率": "90Hz"},
    {"分数": 4, "刷新率": "120Hz"},
    {"分数": 5, "刷新率": "144Hz"},
    {"分数": 6, "刷新率": "165Hz"},
    {"分数": 7, "刷新率": "185Hz"},
    {"分数": 8, "刷新率": "240Hz"},
]

# 3.4 全局/持续触控采样率打分
TOUCH_SAMPLING_CONT = [
    {"分数": 1, "采样率": "60Hz"},
    {"分数": 2, "采样率": "120Hz"},
    {"分数": 3, "采样率": "240Hz"},
    {"分数": 4, "采样率": "300Hz"},
    {"分数": 5, "采样率": "360Hz"},
    {"分数": 6, "采样率": "480Hz"},
    {"分数": 7, "采样率": "720Hz"},
    {"分数": 8, "采样率": "960Hz"},
    {"分数": 9, "采样率": "1440Hz"},
]
# 3.5 瞬时峰值触控采样率打分
TOUCH_SAMPLING_PEAK = [
    {"分数": 1, "采样率": "1000Hz"},
    {"分数": 2, "采样率": "1650Hz"},
    {"分数": 3, "采样率": "2160Hz"},
    {"分数": 4, "采样率": "2500Hz"},
    {"分数": 5, "采样率": "2600Hz"},
    {"分数": 6, "采样率": "3000Hz"},
    {"分数": 7, "采样率": "3200Hz"},
    {"分数": 8, "采样率": "3500Hz"},
    {"分数": 9, "采样率": "3800Hz"},
    {"分数": 10, "采样率": "4000Hz"},
    {"分数": 11, "采样率": "4800Hz"},
]

# 3.6 手动最大亮度打分
BRIGHTNESS_MANUAL = [
    {"分数": 1, "亮度": "300-400nit"},
    {"分数": 2, "亮度": "500-600nit"},
    {"分数": 3, "亮度": "700-800nit"},
    {"分数": 4, "亮度": "800-1000nit"},
    {"分数": 5, "亮度": "1000-1200nit"},
]

# 3.7 局部峰值亮度打分
BRIGHTNESS_LOCAL_PEAK = [
    {"分数": 1, "亮度": "800-1200nit"},
    {"分数": 2, "亮度": "1500-2000nit"},
    {"分数": 3, "亮度": "2500-3000nit"},
    {"分数": 4, "亮度": "3200-4000nit"},
    {"分数": 5, "亮度": "4500-5000nit"},
    {"分数": 6, "亮度": "5500-6000nit"},
    {"分数": 7, "亮度": "6500nit"},
    {"分数": 8, "亮度": "8000nit"},
    {"分数": 9, "亮度": "10000nit"},
]

# 3.8 HBM全屏激发亮度打分
BRIGHTNESS_HBM = [
    {"分数": 1, "亮度": "600-800nit"},
    {"分数": 2, "亮度": "1000-1200nit"},
]

# ==================== 4. 影像系统 ====================

# 4.1 主摄 - 传感器尺寸打分
MAIN_SENSOR_SIZES = [
    {"分数": 16, "尺寸": "1.2英寸"},
    {"分数": 15, "尺寸": "1英寸（1/0.98英寸）"},
    {"分数": 14, "尺寸": "1/1.08英寸"},
    {"分数": 13, "尺寸": "1/1.12英寸"},
    {"分数": 12, "尺寸": "1/1.28英寸"},
    {"分数": 11, "尺寸": "1/1.3英寸"},
    {"分数": 10, "尺寸": "1/1.35英寸"},
    {"分数": 9, "尺寸": "1/1.4英寸"},
    {"分数": 8, "尺寸": "1/1.5英寸"},
    {"分数": 7, "尺寸": "1/1.55英寸"},
    {"分数": 6, "尺寸": "1/1.56英寸"},
    {"分数": 5, "尺寸": "1/1.67英寸"},
    {"分数": 4, "尺寸": "1/1.95英寸"},
    {"分数": 3, "尺寸": "1/2英寸"},
    {"分数": 2, "尺寸": "1/2.5英寸"},
    {"分数": 1, "尺寸": "1/2.88英寸"},
]

# 4.2 主摄 - 像素打分
MAIN_PIXELS = [
    {"分数": 9, "像素": "2亿（200MP）"},
    {"分数": 8, "像素": "1.08亿（108MP）"},
    {"分数": 7, "像素": "6400万（64MP）"},
    {"分数": 6, "像素": "5000万（50MP）"},
    {"分数": 5, "像素": "4800万（48MP）"},
    {"分数": 4, "像素": "3200万（32MP）"},
    {"分数": 3, "像素": "1600万（16MP）"},
    {"分数": 2, "像素": "1300万（13MP）"},
    {"分数": 1, "像素": "1200万（12MP）"},
]

# 4.3 主摄 - 光圈打分
MAIN_APERTURE = [
    {"分数": 13, "光圈": "f/1.4"},
    {"分数": 12, "光圈": "f/1.5"},
    {"分数": 11, "光圈": "f/1.6"},
    {"分数": 10, "光圈": "f/1.63"},
    {"分数": 9, "光圈": "f/1.67"},
    {"分数": 8, "光圈": "f/1.68"},
    {"分数": 7, "光圈": "f/1.7"},
    {"分数": 6, "光圈": "f/1.78"},
    {"分数": 5, "光圈": "f/1.8"},
    {"分数": 4, "光圈": "f/1.85"},
    {"分数": 3, "光圈": "f/1.88"},
    {"分数": 2, "光圈": "f/2.0"},
    {"分数": 1, "光圈": "f/2.2"},
]
# 4.4 主摄 - OIS光学防抖打分（CIPA等级）
MAIN_OIS = [
    {"分数": 9, "等级": "CIPA 7.5"},
    {"分数": 8, "等级": "CIPA 7.0"},
    {"分数": 7, "等级": "CIPA 6.5"},
    {"分数": 6, "等级": "CIPA 6.0"},
    {"分数": 5, "等级": "CIPA 5.5"},
    {"分数": 4, "等级": "CIPA 5.0"},
    {"分数": 3, "等级": "CIPA 4.5"},
    {"分数": 2, "等级": "CIPA 4.0"},
    {"分数": 1, "等级": "CIPA 3.0"},
]

# 4.5 超广角 - 传感器尺寸打分
ULTRA_SENSOR_SIZES = [
    {"分数": 10, "尺寸": "1/1.28英寸"},
    {"分数": 9, "尺寸": "1/1.56英寸"},
    {"分数": 8, "尺寸": "1/1.95英寸"},
    {"分数": 7, "尺寸": "1/2英寸"},
    {"分数": 6, "尺寸": "1/2.5英寸"},
    {"分数": 5, "尺寸": "1/2.55英寸"},
    {"分数": 4, "尺寸": "1/2.75英寸"},
    {"分数": 3, "尺寸": "1/2.88英寸"},
    {"分数": 2, "尺寸": "1/3.06英寸"},
    {"分数": 1, "尺寸": "1/3.6英寸"},
]

# 4.6 超广角 - 视角范围打分
ULTRA_FOV = [
    {"分数": 11, "视角": "123°"},
    {"分数": 10, "视角": "122°"},
    {"分数": 9, "视角": "120°"},
    {"分数": 8, "视角": "116°"},
    {"分数": 7, "视角": "115°"},
    {"分数": 6, "视角": "114°"},
    {"分数": 5, "视角": "112°"},
    {"分数": 4, "视角": "110°"},
    {"分数": 3, "视角": "108°"},
    {"分数": 2, "视角": "107°"},
    {"分数": 1, "视角": "100°"},
]

# 4.7 超广角 - 像素打分
ULTRA_PIXELS = [
    {"分数": 4, "像素": "5000万（50MP）原生像素"},
    {"分数": 3, "像素": "4800万（48MP）原生像素"},
    {"分数": 2, "像素": "4000万（40MP）"},
    {"分数": 1, "像素": "1200万（12MP）默认输出"},
]

# 4.8 超广角 - 光圈打分
ULTRA_APERTURE = [
    {"分数": 7, "光圈": "f/1.6"},
    {"分数": 6, "光圈": "f/1.8"},
    {"分数": 5, "光圈": "f/2.0"},
    {"分数": 4, "光圈": "f/2.05"},
    {"分数": 3, "光圈": "f/2.2"},
    {"分数": 2, "光圈": "f/2.4"},
    {"分数": 1, "光圈": "f/2.6"},
]
# 4.9 超广角 - OIS打分（CIPA等级）
ULTRA_OIS = [
    {"分数": 9, "等级": "CIPA 7.5"},
    {"分数": 8, "等级": "CIPA 7.0"},
    {"分数": 7, "等级": "CIPA 6.5"},
    {"分数": 6, "等级": "CIPA 6.0"},
    {"分数": 5, "等级": "CIPA 5.5"},
    {"分数": 4, "等级": "CIPA 5.0"},
    {"分数": 3, "等级": "CIPA 4.5"},
    {"分数": 2, "等级": "CIPA 4.0"},
    {"分数": 1, "等级": "CIPA 3.0"},
]

# 4.10 长焦 - 像素打分
TELE_PIXELS = [
    {"分数": 8, "像素": "2亿（200MP）"},
    {"分数": 7, "像素": "6400万（64MP）"},
    {"分数": 6, "像素": "5000万（50MP）"},
    {"分数": 5, "像素": "4800万"},
    {"分数": 4, "像素": "1250万"},
    {"分数": 3, "像素": "1200万"},
    {"分数": 2, "像素": "1000万（10MP）"},
    {"分数": 1, "像素": "800万（8MP）"},
]

# 4.11 长焦 - 光学变焦倍数打分
TELE_ZOOM = [
    {"分数": 16, "变焦": "10倍"},
    {"分数": 15, "变焦": "9.4倍"},
    {"分数": 14, "变焦": "7倍"},
    {"分数": 13, "变焦": "6.2倍"},
    {"分数": 12, "变焦": "6倍"},
    {"分数": 11, "变焦": "5倍"},
    {"分数": 10, "变焦": "4.3倍"},
    {"分数": 9, "变焦": "4倍"},
    {"分数": 8, "变焦": "3.7倍"},
    {"分数": 7, "变焦": "3.5倍"},
    {"分数": 6, "变焦": "3.2倍"},
    {"分数": 5, "变焦": "3倍"},
    {"分数": 4, "变焦": "2.9倍"},
    {"分数": 3, "变焦": "2.8倍"},
    {"分数": 2, "变焦": "2.5倍"},
    {"分数": 1, "变焦": "2倍"},
]

# 4.12 长焦 - 传感器尺寸打分
TELE_SENSOR_SIZES = [
    {"分数": 9, "尺寸": "1/1.28英寸"},
    {"分数": 8, "尺寸": "1/1.3英寸"},
    {"分数": 7, "尺寸": "1/1.4英寸"},
    {"分数": 6, "尺寸": "1/1.56英寸"},
    {"分数": 5, "尺寸": "1/2英寸"},
    {"分数": 4, "尺寸": "1/2.5英寸"},
    {"分数": 3, "尺寸": "1/2.52英寸"},
    {"分数": 2, "尺寸": "1/2.75英寸"},
    {"分数": 1, "尺寸": "1/3.2英寸"},
]

# 4.13 长焦 - OIS打分（CIPA等级）
TELE_OIS = [
    {"分数": 9, "等级": "CIPA 7.5"},
    {"分数": 8, "等级": "CIPA 7.0"},
    {"分数": 7, "等级": "CIPA 6.5"},
    {"分数": 6, "等级": "CIPA 6.0"},
    {"分数": 5, "等级": "CIPA 5.5"},
    {"分数": 4, "等级": "CIPA 5.0"},
    {"分数": 3, "等级": "CIPA 4.5"},
    {"分数": 2, "等级": "CIPA 4.0"},
    {"分数": 1, "等级": "CIPA 3.0"},
]

# 4.14 前置 - 广角传感器像素打分
FRONT_WIDE_PIXELS = [
    {"分数": 12, "像素": "2亿（200MP）"},
    {"分数": 11, "像素": "6800万（68MP）"},
    {"分数": 10, "像素": "6000万（60MP）"},
    {"分数": 9, "像素": "5000万（50MP）"},
    {"分数": 8, "像素": "4400万（44MP）"},
    {"分数": 7, "像素": "3200万（32MP）"},
    {"分数": 6, "像素": "2400万（24MP）"},
    {"分数": 5, "像素": "1800万（18MP）"},
    {"分数": 4, "像素": "1300万（13MP）"},
    {"分数": 3, "像素": "1200万（12MP）"},
    {"分数": 2, "像素": "1000万（10MP）"},
    {"分数": 1, "像素": "800万（8MP）"},
]

# 4.15 前置 - 视角范围打分
FRONT_FOV = [
    {"分数": 7, "视角": "110°"},
    {"分数": 6, "视角": "105°"},
    {"分数": 5, "视角": "100°"},
    {"分数": 4, "视角": "95°"},
    {"分数": 3, "视角": "92°"},
    {"分数": 2, "视角": "90°"},
    {"分数": 1, "视角": "89.6°"},
]

# 4.16 前置 - 传感器尺寸打分
FRONT_SENSOR_SIZES = [
    {"分数": 10, "尺寸": "1/2.0英寸"},
    {"分数": 9, "尺寸": "1/2.5英寸"},
    {"分数": 8, "尺寸": "1/2.55英寸"},
    {"分数": 7, "尺寸": "1/2.75英寸"},
    {"分数": 6, "尺寸": "1/2.76英寸"},
    {"分数": 5, "尺寸": "1/2.8英寸"},
    {"分数": 4, "尺寸": "1/2.93英寸"},
    {"分数": 3, "尺寸": "1/3.6英寸"},
]

# 4.17 前置 - 像素打分
FRONT_PIXELS = [
    {"分数": 12, "像素": "2亿（200MP）"},
    {"分数": 11, "像素": "6800万（68MP）"},
    {"分数": 10, "像素": "6000万（60MP）"},
    {"分数": 9, "像素": "5000万（50MP）"},
    {"分数": 8, "像素": "4400万（44MP）"},
    {"分数": 7, "像素": "3200万（32MP）"},
    {"分数": 6, "像素": "2400万（24MP）"},
    {"分数": 5, "像素": "1800万（18MP）"},
    {"分数": 4, "像素": "1300万（13MP）"},
    {"分数": 3, "像素": "1200万（12MP）"},
    {"分数": 2, "像素": "1000万（10MP）"},
    {"分数": 1, "像素": "800万（8MP）"},
]

# ==================== 5. 能源系统 ====================

# 5.1 电池标称容量打分
BATTERY_CAPACITY = [
    {"分数": 6, "区间": "≥10000mAh"},
    {"分数": 5, "区间": "8000~9999mAh"},
    {"分数": 4, "区间": "7000~7999mAh"},
    {"分数": 3, "区间": "5500~6999mAh"},
    {"分数": 2, "区间": "4500~5499mAh"},
    {"分数": 1, "区间": "<4500mAh"},
]

# 5.2 电池能量密度打分
BATTERY_DENSITY = [
    {"分数": 6, "区间": "≥950 Wh/L"},
    {"分数": 5, "区间": "900-949 Wh/L"},
    {"分数": 4, "区间": "800~899 Wh/L"},
    {"分数": 3, "区间": "750~799 Wh/L"},
    {"分数": 2, "区间": "650~749 Wh/L"},
    {"分数": 1, "区间": "<650 Wh/L"},
]

# 5.3 有线充电功率打分
WIRED_CHARGING = [
    {"分数": 6, "区间": "≥200W"},
    {"分数": 5, "区间": "150~199W"},
    {"分数": 4, "区间": "100~149W"},
    {"分数": 3, "区间": "80~99W"},
    {"分数": 2, "区间": "40~79W"},
    {"分数": 1, "区间": "≤40W"},
]

# 5.4 无线充电功率打分
WIRELESS_CHARGING = [
    {"分数": 5, "区间": "≥80W"},
    {"分数": 4, "区间": "50~79W"},
    {"分数": 3, "区间": "30~49W"},
    {"分数": 2, "区间": "15~29W"},
    {"分数": 1, "区间": "≤15W"},
]

# 5.5 反向无线充电打分
REVERSE_WIRELESS_CHARGING = [
    {"分数": 5, "区间": "≥20W"},
    {"分数": 4, "区间": "15~19W"},
    {"分数": 3, "区间": "10~14W"},
    {"分数": 2, "区间": "5~9W"},
    {"分数": 1, "区间": "<5W"},
]

# ==================== 6. 机身结构 ====================

# 6.1 中框材质打分
FRAME_MATERIALS = [
    {"分数": 9, "材质": "钛合金（Grade 5/TC4）"},
    {"分数": 8, "材质": "7系高强铝合金（7075系）一体成型"},
    {"分数": 7, "材质": "6系航空铝合金（6M13/6063系）CNC一体成型"},
    {"分数": 6, "材质": "Armor Aluminum（三星定制铝合金）"},
    {"分数": 5, "材质": "航空铝一体化中框（自研架构）"},
    {"分数": 4, "材质": "高分子与金属复合材料一体成型"},
    {"分数": 3, "材质": "压铸一体成型中框（铝+不锈钢复合）"},
    {"分数": 2, "材质": "不锈钢（316L/手术级）"},
    {"分数": 1, "材质": "工程塑料（PC+ABS/聚碳酸酯）"},
]

# 6.3 机身重量打分
DEVICE_WEIGHT = [
    {"分数": 6, "区间": "≤165g"},
    {"分数": 5, "区间": "166~180g"},
    {"分数": 4, "区间": "181~195g"},
    {"分数": 3, "区间": "196~215g"},
    {"分数": 2, "区间": "216~235g"},
    {"分数": 1, "区间": "236~260g"},
]

# 6.4 IP防护等级打分
IP_RATING = [
    {"分数": 8, "等级": "IP68+IP69+IP69K"},
    {"分数": 7, "等级": "IP68+IP69K"},
    {"分数": 6, "等级": "IP68+IP69"},
    {"分数": 5, "等级": "IP68"},
    {"分数": 4, "等级": "IP67"},
    {"分数": 3, "等级": "IP66/IP65"},
    {"分数": 2, "等级": "IP54/IP53"},
    {"分数": 1, "等级": "无认证/IP52及以下"},
]

# 6.5 VC均热板面积打分
VC_HEAT_PIPE = [
    {"分数": 7, "区间": "≥15000mm²"},
    {"分数": 6, "区间": "10000~14999mm²"},
    {"分数": 5, "区间": "8000~9999mm²"},
    {"分数": 4, "区间": "6000~7999mm²"},
    {"分数": 3, "区间": "5000~5999mm²"},
    {"分数": 2, "区间": "3000~4999mm²"},
    {"分数": 1, "区间": "<3000mm²"},
]

# 6.6 石墨烯散热层打分
GRAPHENE_COOLING = [
    {"分数": 4, "类型": "单层超高导热石墨烯膜"},
    {"分数": 3, "类型": "多层次石墨烯复合膜"},
    {"分数": 2, "类型": "传统多层人工石墨膜"},
    {"分数": 1, "类型": "基础石墨散热片"},
]

# ==================== 7. 通信模块 ====================

# 7.1 Wi-Fi模块打分
WIFI_MODULES = [
    {"分数": 5, "版本": "Wi-Fi 7(802.11be)"},
    {"分数": 4, "版本": "Wi-Fi 6E (802.11ax)"},
    {"分数": 3, "版本": "Wi-Fi 6(802.11ax)"},
    {"分数": 2, "版本": "Wi-Fi 5(802.11ac)"},
    {"分数": 1, "版本": "Wi-Fi 4(802.11n)"},
]

# 7.2 蓝牙模块打分
BLUETOOTH_MODULES = [
    {"分数": 4, "版本": "蓝牙 6.0"},
    {"分数": 3, "版本": "蓝牙 5.4"},
    {"分数": 2, "版本": "蓝牙 5.3"},
    {"分数": 1, "版本": "蓝牙 5.2"},
]

# ==================== 8. 其他硬件 ====================

# 8.1 USB Type-C接口打分
USB_C_INTERFACES = [
    {"分数": 5, "协议": "USB4 Gen 3×2"},
    {"分数": 4, "协议": "USB 3.2 Gen 2×2"},
    {"分数": 3, "协议": "USB 3.2 Gen 2×1"},
    {"分数": 2, "协议": "USB 3.2 Gen 1×1"},
    {"分数": 1, "协议": "USB 2.0"},
]

# 8.2 USB视频输出打分（修复：DP版本越高分数越高）
USB_VIDEO_OUTPUT = [
    {"分数": 1, "协议": "DP 1.2 Alt Mode"},
    {"分数": 2, "协议": "DP 1.4 Alt Mode"},
    {"分数": 3, "协议": "DP 2.1 Alt Mode"},
]

# 8.3 SIM卡槽打分
SIM_SLOTS = [
    {"分数": 7, "方案": "双Nano-SIM + 双eSIM"},
    {"分数": 6, "方案": "独立三卡槽（双SIM+TF）"},
    {"分数": 5, "方案": "双Nano-SIM（传统双卡槽）"},
    {"分数": 4, "方案": "三选二卡槽（与或卡槽）"},
    {"分数": 3, "方案": "单Nano-SIM + 双eSIM"},
    {"分数": 2, "方案": "纯eSIM（eSIM-only）"},
    {"分数": 1, "方案": "单Nano-SIM"},
]

# 8.4 扬声器单元打分
SPEAKERS = [
    {"分数": 6, "方案": "2.1声道系统（对称双扬+独立低音炮）"},
    {"分数": 5, "方案": "同轴共磁路对称双扬声器"},
    {"分数": 4, "方案": "超导磁线性立体声双扬声器"},
    {"分数": 3, "方案": "1115F/1216对称式双扬声器"},
    {"分数": 2, "方案": "非对称双扬声器（听筒复用）"},
    {"分数": 1, "方案": "单扬声器（底部）"},
]

# ==================== 9. 简单计分规则 ====================
# 类型说明：
# "has" = 有/无打分（有=得分，无=0分）
# "count" = 按数量打分（多少个加多少分，用户输入的数字就是分数）
# "select" = 从多个选项中选一个打分

SIMPLE_SCORING = [
    # 一、核心计算单元 > 处理器（SoC）
    {"大类": "一、核心计算单元", "子类别": "处理器（SoC）", "硬件项": "影像协处理器", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "一、核心计算单元", "子类别": "处理器（SoC）", "硬件项": "AI协处理器", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "一、核心计算单元", "子类别": "处理器（SoC）", "硬件项": "安全协处理器", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "一、核心计算单元", "子类别": "处理器（SoC）", "硬件项": "游戏独显芯片", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "一、核心计算单元", "子类别": "处理器（SoC）", "硬件项": "触控IC", "规则": "有", "分数": 1, "类型": "has"},
    # 二、显示系统 > 屏幕模组
    {"大类": "二、显示系统", "子类别": "屏幕模组", "硬件项": "ppi", "规则": ">450", "分数": 3, "类型": "select"},
    {"大类": "二、显示系统", "子类别": "屏幕模组", "硬件项": "ppi", "规则": "350-450", "分数": 2, "类型": "select"},
    {"大类": "二、显示系统", "子类别": "屏幕模组", "硬件项": "ppi", "规则": "<350", "分数": 1, "类型": "select"},
    {"大类": "二、显示系统", "子类别": "防护玻璃", "硬件项": "盖板材质", "规则": "有强化玻璃", "分数": 1, "类型": "has"},
    {"大类": "二、显示系统", "子类别": "屏幕模组", "硬件项": "疏油层", "规则": "纳米级疏油层", "分数": 3, "类型": "select"},
    {"大类": "二、显示系统", "子类别": "屏幕模组", "硬件项": "疏油层", "规则": "常规疏油层", "分数": 2, "类型": "select"},
    {"大类": "二、显示系统", "子类别": "屏幕模组", "硬件项": "疏油层", "规则": "无", "分数": 1, "类型": "select"},
    # 三、影像系统
    {"大类": "三、影像系统", "子类别": "后置摄像头-超广角", "硬件项": "自动对焦/微距", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "三、影像系统", "子类别": "后置摄像头-长焦", "硬件项": "激光对焦传感器", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "三、影像系统", "子类别": "后置摄像头-辅助传感器", "硬件项": "色温传感器", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "三、影像系统", "子类别": "后置摄像头-辅助传感器", "硬件项": "Flicker传感器", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "三、影像系统", "子类别": "后置摄像头-辅助传感器", "硬件项": "多光谱传感器", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "三、影像系统", "子类别": "前置摄像头", "硬件项": "自动对焦（AF）", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "三、影像系统", "子类别": "前置摄像头", "硬件项": "3D结构光模块", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "三、影像系统", "子类别": "前置摄像头", "硬件项": "深感摄像头", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "三、影像系统", "子类别": "光学组件", "硬件项": "镜头组", "规则": "蓝宝石", "分数": 3, "类型": "select"},
    {"大类": "三、影像系统", "子类别": "光学组件", "硬件项": "镜头组", "规则": "强化玻璃", "分数": 2, "类型": "select"},
    {"大类": "三、影像系统", "子类别": "光学组件", "硬件项": "镜头组", "规则": "塑料", "分数": 1, "类型": "select"},
    {"大类": "三、影像系统", "子类别": "光学组件", "硬件项": "闪光灯", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "三、影像系统", "子类别": "光学组件", "硬件项": "镀膜技术", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "三、影像系统", "子类别": "光学组件", "硬件项": "OIS光学防抖马达", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "三、影像系统", "子类别": "光学组件", "硬件项": "自研影像芯片", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "三、影像系统", "子类别": "影像附加硬件", "硬件项": "物理变焦环", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "三、影像系统", "子类别": "影像附加硬件", "硬件项": "色彩摄像头", "规则": "有", "分数": 1, "类型": "has"},
    # 四、能源系统
    {"大类": "四、能源系统", "子类别": "电池", "硬件项": "双电芯设计", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "四、能源系统", "子类别": "充电模块-有线", "硬件项": "充电兼容档位", "规则": "多少", "分数": "多少", "类型": "count"},
    {"大类": "四、能源系统", "子类别": "电源管理芯片", "硬件项": "电源管理芯片(PMIC)", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "四、能源系统", "子类别": "电源管理芯片", "硬件项": "电池管理芯片", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "四、能源系统", "子类别": "电源管理芯片", "硬件项": "快充芯片", "规则": "有", "分数": 1, "类型": "has"},
    # 五、机身结构
    {"大类": "五、机身结构", "子类别": "外壳材质", "硬件项": "背板材质", "规则": "特殊材质", "分数": 2, "类型": "select"},
    {"大类": "五、机身结构", "子类别": "外壳材质", "硬件项": "背板材质", "规则": "塑料", "分数": 1, "类型": "select"},
    {"大类": "五、机身结构", "子类别": "散热系统", "硬件项": "主动散热", "规则": "有", "分数": 1, "类型": "has"},
    # 六、通信模块
    {"大类": "六、通信模块", "子类别": "蜂窝网络", "硬件项": "频段支持", "规则": "多少", "分数": "多少", "类型": "count"},
    {"大类": "六、通信模块", "子类别": "蜂窝网络", "硬件项": "射频增强芯片", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "六、通信模块", "子类别": "短距离通信", "硬件项": "NFC芯片", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "六、通信模块", "子类别": "短距离通信", "硬件项": "红外遥控", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "六、通信模块", "子类别": "短距离通信", "硬件项": "星闪模块", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "六、通信模块", "子类别": "卫星通信", "硬件项": "天通卫星芯片", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "六、通信模块", "子类别": "卫星通信", "硬件项": "北斗卫星芯片", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "六、通信模块", "子类别": "GPS/GNSS", "硬件项": "GPS/GNSS", "规则": "多少", "分数": "多少", "类型": "count"},
    {"大类": "六、通信模块", "子类别": "卫星通信", "硬件项": "卫星通话/短信", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "六、通信模块", "子类别": "短距离通信", "硬件项": "UWB超宽带芯片", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "六、通信模块", "子类别": "蜂窝网络", "硬件项": "eSIM芯片", "规则": "有", "分数": 1, "类型": "has"},
    # 七、传感器系统
    {"大类": "七、传感器系统", "子类别": "环境感知", "硬件项": "光线传感器", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "七、传感器系统", "子类别": "环境感知", "硬件项": "气压计", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "七、传感器系统", "子类别": "环境感知", "硬件项": "湿度传感器", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "七、传感器系统", "子类别": "环境感知", "硬件项": "空气质量传感器", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "七、传感器系统", "子类别": "环境感知", "硬件项": "紫外线传感器", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "七、传感器系统", "子类别": "运动感知", "硬件项": "陀螺仪", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "七、传感器系统", "子类别": "运动感知", "硬件项": "加速度传感器", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "七、传感器系统", "子类别": "运动感知", "硬件项": "指南针/电子罗盘", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "七、传感器系统", "子类别": "生物识别", "硬件项": "指纹传感器类型", "规则": "超声波", "分数": 4, "类型": "select"},
    {"大类": "七、传感器系统", "子类别": "生物识别", "硬件项": "指纹传感器类型", "规则": "超薄光学", "分数": 3, "类型": "select"},
    {"大类": "七、传感器系统", "子类别": "生物识别", "硬件项": "指纹传感器类型", "规则": "短焦光学", "分数": 2, "类型": "select"},
    {"大类": "七、传感器系统", "子类别": "生物识别", "硬件项": "指纹传感器类型", "规则": "侧边电容", "分数": 1, "类型": "select"},
    {"大类": "七、传感器系统", "子类别": "辅助传感器", "硬件项": "红外传感器", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "七、传感器系统", "子类别": "辅助传感器", "硬件项": "霍尔传感器", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "七、传感器系统", "子类别": "辅助传感器", "硬件项": "距离传感器", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "七、传感器系统", "子类别": "辅助传感器", "硬件项": "心率传感器", "规则": "有", "分数": 1, "类型": "has"},
    # 八、其他硬件
    {"大类": "八、其他硬件", "子类别": "音频系统", "硬件项": "音频解码芯片", "规则": "有", "分数": 1, "类型": "has"},
    {"大类": "八、其他硬件", "子类别": "音频系统", "硬件项": "麦克风阵列", "规则": "多少", "分数": "多少", "类型": "count"},
    {"大类": "八、其他硬件", "子类别": "接口与扩展", "硬件项": "3.5mm耳机孔", "规则": "有", "分数": 1, "类型": "has"},
]

# ==================== ScoringEngine 类 ====================
class ScoringEngine:
    """手机硬件打分引擎"""
    def __init__(self):
        self.soc_scores = SOC_SCORES
        self.ram_types = RAM_TYPES
        self.ram_capacity_tiers = RAM_CAPACITY_TIERS
        self.rom_types = ROM_TYPES
        self.capacity_tiers = CAPACITY_TIERS
        self.expand_storage = EXPAND_STORAGE
        self.nm_card_bonus = NM_CARD_BONUS
        # 显示系统
        self.panel_types = PANEL_TYPES
        self.resolutions = RESOLUTIONS
        self.refresh_rates = REFRESH_RATES
        self.touch_sampling_cont = TOUCH_SAMPLING_CONT
        self.touch_sampling_peak = TOUCH_SAMPLING_PEAK
        self.brightness_manual = BRIGHTNESS_MANUAL
        self.brightness_local_peak = BRIGHTNESS_LOCAL_PEAK
        self.brightness_hbm = BRIGHTNESS_HBM
        # 影像系统
        self.main_sensor_sizes = MAIN_SENSOR_SIZES
        self.main_pixels = MAIN_PIXELS
        self.main_aperture = MAIN_APERTURE
        self.main_ois = MAIN_OIS
        self.ultra_sensor_sizes = ULTRA_SENSOR_SIZES
        self.ultra_fov = ULTRA_FOV
        self.ultra_pixels = ULTRA_PIXELS
        self.ultra_aperture = ULTRA_APERTURE
        self.ultra_ois = ULTRA_OIS
        self.tele_pixels = TELE_PIXELS
        self.tele_zoom = TELE_ZOOM
        self.tele_sensor_sizes = TELE_SENSOR_SIZES
        self.tele_ois = TELE_OIS
        self.front_wide_pixels = FRONT_WIDE_PIXELS
        self.front_fov = FRONT_FOV
        self.front_sensor_sizes = FRONT_SENSOR_SIZES
        self.front_pixels = FRONT_PIXELS
        # 能源系统
        self.battery_capacity = BATTERY_CAPACITY
        self.battery_density = BATTERY_DENSITY
        self.wired_charging = WIRED_CHARGING
        self.wireless_charging = WIRELESS_CHARGING
        self.reverse_wireless_charging = REVERSE_WIRELESS_CHARGING
        # 机身结构
        self.frame_materials = FRAME_MATERIALS
        self.device_weight = DEVICE_WEIGHT
        self.ip_rating = IP_RATING
        self.vc_heat_pipe = VC_HEAT_PIPE
        self.graphene_cooling = GRAPHENE_COOLING
        # 通信模块
        self.wifi_modules = WIFI_MODULES
        self.bluetooth_modules = BLUETOOTH_MODULES
        # 其他硬件
        self.usb_c_interfaces = USB_C_INTERFACES
        self.usb_video_output = USB_VIDEO_OUTPUT
        self.sim_slots = SIM_SLOTS
        self.speakers = SPEAKERS
        # 简单计分
        self.simple_scoring = SIMPLE_SCORING

    # ==================== 查询方法（供前端下拉菜单使用） ====================
    def get_categories(self):
        """获取所有大类"""
        return [
            "一、核心计算单元",
            "二、显示系统",
            "三、影像系统",
            "四、能源系统",
            "五、机身结构",
            "六、通信模块",
            "七、传感器系统",
            "八、其他硬件",
        ]

    def get_soc_options(self):
        """获取SoC可选列表（供下拉菜单）"""
        return [{"型号": s["型号"], "分数": s["分数"]} for s in self.soc_scores]

    def get_ram_options(self):
        """获取RAM可选列表"""
        return [{"版本": r["版本"], "分数": r["分数"]} for r in self.ram_types]

    def get_ram_capacity_options(self):
        """获取RAM容量可选列表"""
        return [{"容量_GB": c["容量_GB"], "分数": c["分数"]} for c in self.ram_capacity_tiers]
    def get_rom_options(self):
        """获取ROM/存储版本可选列表"""
        return [{"类型": r["类型"], "版本": r["版本"], "分数": r["分数"]} for r in self.rom_types]

    def get_capacity_options(self):
        """获取存储容量可选列表"""
        return [{"容量_GB": c["容量_GB"], "分数": c["分数"]} for c in self.capacity_tiers]

    def get_expand_storage_options(self):
        """获取扩展内存可选列表（修复：分为卡类型和容量两个独立选择）
        返回格式:
        - card_types: [{"type": "无"},{"type": "TF卡"}, {"type": "华为NM卡(+1分)"}]
        - tf_capacities: [{"容量_GB": 64, "分数": 1}, ...]  # TF卡容量档位
        - nm_capacities: [{"容量_GB": 64, "分数": 2}, ...]  # NM卡容量档位（+1分）
        """
        tf_caps = [{"容量_GB": e["容量_GB"], "分数": e["分数"]} for e in self.expand_storage]
        nm_caps = [{"容量_GB": e["容量_GB"], "分数": e["分数"] + self.nm_card_bonus} for e in self.expand_storage]
        return {
            "card_types": [
                {"type": "无", "说明": "不支持扩展存储"},
                {"type": "TF卡", "说明": "MicroSD卡"},
                {"type": "华为NM卡", "说明": "华为NM卡（同容量+1分）"},
            ],
            "tf_capacities": tf_caps,
            "nm_capacities": nm_caps,
        }

    # 修复：get_panel_options 使用字典格式
    def get_panel_options(self):
        """获取显示面板可选列表"""
        return [{"类型": p["类型"], "分数": p["分数"]} for p in self.panel_types]

    def get_resolution_options(self):
        """获取分辨率可选列表"""
        return [{"分辨率": r["分辨率"], "分数": r["分数"]} for r in self.resolutions]

    def get_refresh_rate_options(self):
        """获取刷新率可选列表"""
        return [{"刷新率": r["刷新率"], "分数": r["分数"]} for r in self.refresh_rates]

    def get_touch_sampling_cont_options(self):
        """获取全局/持续触控采样率可选列表"""
        return [{"采样率": t["采样率"], "分数": t["分数"]} for t in self.touch_sampling_cont]

    def get_touch_sampling_peak_options(self):
        """获取瞬时峰值触控采样率可选列表"""
        return [{"采样率": t["采样率"], "分数": t["分数"]} for t in self.touch_sampling_peak]

    def get_brightness_manual_options(self):
        """获取手动最大亮度可选列表"""
        return [{"亮度": b["亮度"], "分数": b["分数"]} for b in self.brightness_manual]

    def get_brightness_local_peak_options(self):
        """获取局部峰值亮度可选列表"""
        return [{"亮度": b["亮度"], "分数": b["分数"]} for b in self.brightness_local_peak]

    def get_brightness_hbm_options(self):
        """获取HBM全屏激发亮度可选列表"""
        return [{"亮度": b["亮度"], "分数": b["分数"]} for b in self.brightness_hbm]

    # 影像系统查询方法
    def get_main_sensor_size_options(self):
        return [{"尺寸": s["尺寸"], "分数": s["分数"]} for s in self.main_sensor_sizes]

    def get_main_pixel_options(self):
        return [{"像素": p["像素"], "分数": p["分数"]} for p in self.main_pixels]

    def get_main_aperture_options(self):
        return [{"光圈": a["光圈"], "分数": a["分数"]} for a in self.main_aperture]

    def get_main_ois_options(self):
        return [{"等级": o["等级"], "分数": o["分数"]} for o in self.main_ois]

    def get_ultra_sensor_size_options(self):
        return [{"尺寸": s["尺寸"], "分数": s["分数"]} for s in self.ultra_sensor_sizes]

    def get_ultra_fov_options(self):
        return [{"视角": f["视角"], "分数": f["分数"]} for f in self.ultra_fov]

    def get_ultra_pixel_options(self):
        return [{"像素": p["像素"], "分数": p["分数"]} for p in self.ultra_pixels]

    def get_ultra_aperture_options(self):
        return [{"光圈": a["光圈"], "分数": a["分数"]} for a in self.ultra_aperture]

    def get_ultra_ois_options(self):
        return [{"等级": o["等级"], "分数": o["分数"]} for o in self.ultra_ois]

    def get_tele_pixel_options(self):
        return [{"像素": p["像素"], "分数": p["分数"]} for p in self.tele_pixels]

    def get_tele_zoom_options(self):
        return [{"变焦": z["变焦"], "分数": z["分数"]} for z in self.tele_zoom]

    def get_tele_sensor_size_options(self):
        return [{"尺寸": s["尺寸"], "分数": s["分数"]} for s in self.tele_sensor_sizes]

    def get_tele_ois_options(self):
        return [{"等级": o["等级"], "分数": o["分数"]} for o in self.tele_ois]

    def get_front_wide_pixel_options(self):
        return [{"像素": p["像素"], "分数": p["分数"]} for p in self.front_wide_pixels]

    def get_front_fov_options(self):
        return [{"视角": f["视角"], "分数": f["分数"]} for f in self.front_fov]

    def get_front_sensor_size_options(self):
        return [{"尺寸": s["尺寸"], "分数": s["分数"]} for s in self.front_sensor_sizes]

    def get_front_pixel_options(self):
        return [{"像素": p["像素"], "分数": p["分数"]} for p in self.front_pixels]

    # 能源系统查询方法
    def get_battery_capacity_options(self):
        return [{"区间": b["区间"], "分数": b["分数"]} for b in self.battery_capacity]

    def get_battery_density_options(self):
        return [{"区间": b["区间"], "分数": b["分数"]} for b in self.battery_density]

    def get_wired_charging_options(self):
        return [{"区间": w["区间"], "分数": w["分数"]} for w in self.wired_charging]

    def get_wireless_charging_options(self):
        return [{"区间": w["区间"], "分数": w["分数"]} for w in self.wireless_charging]

    def get_reverse_wireless_charging_options(self):
        return [{"区间": w["区间"], "分数": w["分数"]} for w in self.reverse_wireless_charging]

    # 机身结构查询方法
    def get_frame_material_options(self):
        return [{"材质": f["材质"], "分数": f["分数"]} for f in self.frame_materials]

    def get_device_weight_options(self):
        return [{"区间": w["区间"], "分数": w["分数"]} for w in self.device_weight]

    def get_ip_rating_options(self):
        return [{"等级": i["等级"], "分数": i["分数"]} for i in self.ip_rating]

    def get_vc_heat_pipe_options(self):
        return [{"区间": v["区间"], "分数": v["分数"]} for v in self.vc_heat_pipe]

    def get_graphene_cooling_options(self):
        return [{"类型": g["类型"], "分数": g["分数"]} for g in self.graphene_cooling]

    # 通信模块查询方法
    def get_wifi_options(self):
        return [{"版本": w["版本"], "分数": w["分数"]} for w in self.wifi_modules]

    def get_bluetooth_options(self):
        return [{"版本": b["版本"], "分数": b["分数"]} for b in self.bluetooth_modules]

    # 其他硬件查询方法
    def get_usb_c_options(self):
        return [{"协议": u["协议"], "分数": u["分数"]} for u in self.usb_c_interfaces]

    def get_usb_video_options(self):
        return [{"协议": u["协议"], "分数": u["分数"]} for u in self.usb_video_output]

    def get_sim_slot_options(self):
        return [{"方案": s["方案"], "分数": s["分数"]} for s in self.sim_slots]

    def get_speaker_options(self):
        return [{"方案": s["方案"], "分数": s["分数"]} for s in self.speakers]

    # 简单计分查询方法
    def get_simple_scoring_options(self):
        """获取所有简单计分规则"""
        return self.simple_scoring

    def get_simple_scoring_by_category(self, category):
        """按大类获取简单计分规则"""
        return [s for s in self.simple_scoring if s["大类"] == category]

    # ==================== 计算方法 ====================

    # 修复1: calc_soc_score - 精确匹配（前端下拉选择，不存在模糊匹配误判）
    def calc_soc_score(self, chip_name):
        """根据SoC型号计算分数（精确匹配，前端下拉选择）"""
        # 精确匹配（前端下拉选择，值应该完全匹配）
        for s in self.soc_scores:
            if chip_name.strip() == s["型号"]:
                return s["分数"]
        # 大小写不敏感匹配（备用容错）
        chip_norm = chip_name.strip().lower()
        for s in self.soc_scores:
            if chip_norm == s["型号"].strip().lower():
                return s["分数"]
        return 0

    def calc_ram_score(self, ram_version):
        """根据RAM版本计算分数"""
        for r in self.ram_types:
            if ram_version.strip() == r["版本"]:
                return r["分数"]
        return 0

    def calc_ram_capacity_score(self, capacity_gb):
        """根据RAM容量计算分数"""
        for c in self.ram_capacity_tiers:
            if c["容量_GB"] == capacity_gb:
                return c["分数"]
        for c in sorted(self.ram_capacity_tiers, key=lambda x: x["容量_GB"], reverse=True):
            if capacity_gb >= c["容量_GB"]:
                return c["分数"]
        return 0

    def calc_rom_score(self, rom_version):
        """根据ROM版本计算分数"""
        for r in self.rom_types:
            if rom_version.strip() == r["版本"]:
                return r["分数"]
        return 0

    def calc_capacity_score(self, capacity_gb):
        """根据存储容量计算分数"""
        for c in self.capacity_tiers:
            if c["容量_GB"] == capacity_gb:
                return c["分数"]
        for c in sorted(self.capacity_tiers, key=lambda x: x["容量_GB"], reverse=True):
            if capacity_gb >= c["容量_GB"]:
                return c["分数"]
        return 0

    # 修复3: calc_expand_storage_score - 拆分为卡类型+容量两个独立参数
    def calc_expand_storage_score(self, card_type, capacity_gb):
        """计算扩展内存分数
        card_type: "无" / "TF卡" / "华为NM卡"
        capacity_gb: 支持的存储卡最大容量（GB）
        """
        if card_type == "无":
            return 0
        base_score = 0
        for e in self.expand_storage:
            if e["容量_GB"] == capacity_gb:
                base_score = e["分数"]
                break
        if card_type == "华为NM卡":
            base_score += self.nm_card_bonus
        return base_score

    # 修复5: calc_panel_score - 新增面板类型打分方法
    def calc_panel_score(self, panel_type):
        """根据显示面板类型计算分数"""
        for p in self.panel_types:
            if panel_type.strip() == p["类型"]:
                return p["分数"]
        return 0

    def calc_resolution_score(self, resolution):
        """根据分辨率计算分数"""
        for r in self.resolutions:
            if resolution.strip() == r["分辨率"]:
                return r["分数"]
        return 0

    def calc_refresh_rate_score(self, refresh_rate):
        """根据刷新率计算分数"""
        for r in self.refresh_rates:
            if refresh_rate.strip() == r["刷新率"]:
                return r["分数"]
        return 0

    def calc_touch_sampling_cont_score(self, sampling_rate):
        """根据全局/持续触控采样率计算分数"""
        for t in self.touch_sampling_cont:
            if sampling_rate.strip() == t["采样率"]:
                return t["分数"]
        return 0

    def calc_touch_sampling_peak_score(self, sampling_rate):
        """根据瞬时峰值触控采样率计算分数"""
        for t in self.touch_sampling_peak:
            if sampling_rate.strip() == t["采样率"]:
                return t["分数"]
        return 0

    def calc_brightness_manual_score(self, brightness):
        """根据手动最大亮度计算分数"""
        for b in self.brightness_manual:
            if brightness.strip() == b["亮度"]:
                return b["分数"]
        return 0

    def calc_brightness_local_peak_score(self, brightness):
        """根据局部峰值亮度计算分数"""
        for b in self.brightness_local_peak:
            if brightness.strip() == b["亮度"]:
                return b["分数"]
        return 0

    def calc_brightness_hbm_score(self, brightness):
        """根据HBM全屏激发亮度计算分数"""
        for b in self.brightness_hbm:
            if brightness.strip() == b["亮度"]:
                return b["分数"]
        return 0

    # 影像系统打分方法
    def calc_main_sensor_size_score(self, size):
        for s in self.main_sensor_sizes:
            if size.strip() == s["尺寸"]:
                return s["分数"]
        return 0

    def calc_main_pixel_score(self, pixel):
        for p in self.main_pixels:
            if pixel.strip() == p["像素"]:
                return p["分数"]
        return 0

    def calc_main_aperture_score(self, aperture):
        for a in self.main_aperture:
            if aperture.strip() == a["光圈"]:
                return a["分数"]
        return 0

    def calc_main_ois_score(self, level):
        for o in self.main_ois:
            if level.strip() == o["等级"]:
                return o["分数"]
        return 0

    def calc_ultra_sensor_size_score(self, size):
        for s in self.ultra_sensor_sizes:
            if size.strip() == s["尺寸"]:
                return s["分数"]
        return 0

    def calc_ultra_fov_score(self, fov):
        for f in self.ultra_fov:
            if fov.strip() == f["视角"]:
                return f["分数"]
        return 0

    def calc_ultra_pixel_score(self, pixel):
        for p in self.ultra_pixels:
            if pixel.strip() == p["像素"]:
                return p["分数"]
        return 0

    def calc_ultra_aperture_score(self, aperture):
        for a in self.ultra_aperture:
            if aperture.strip() == a["光圈"]:
                return a["分数"]
        return 0

    def calc_ultra_ois_score(self, level):
        for o in self.ultra_ois:
            if level.strip() == o["等级"]:
                return o["分数"]
        return 0

    def calc_tele_pixel_score(self, pixel):
        for p in self.tele_pixels:
            if pixel.strip() == p["像素"]:
                return p["分数"]
        return 0

    def calc_tele_zoom_score(self, zoom):
        for z in self.tele_zoom:
            if zoom.strip() == z["变焦"]:
                return z["分数"]
        return 0

    def calc_tele_sensor_size_score(self, size):
        for s in self.tele_sensor_sizes:
            if size.strip() == s["尺寸"]:
                return s["分数"]
        return 0

    def calc_tele_ois_score(self, level):
        for o in self.tele_ois:
            if level.strip() == o["等级"]:
                return o["分数"]
        return 0

    def calc_front_wide_pixel_score(self, pixel):
        for p in self.front_wide_pixels:
            if pixel.strip() == p["像素"]:
                return p["分数"]
        return 0

    def calc_front_fov_score(self, fov):
        for f in self.front_fov:
            if fov.strip() == f["视角"]:
                return f["分数"]
        return 0

    def calc_front_sensor_size_score(self, size):
        for s in self.front_sensor_sizes:
            if size.strip() == s["尺寸"]:
                return s["分数"]
        return 0

    def calc_front_pixel_score(self, pixel):
        for p in self.front_pixels:
            if pixel.strip() == p["像素"]:
                return p["分数"]
        return 0

    # 能源系统打分方法
    def calc_battery_capacity_score(self, capacity):
        for b in self.battery_capacity:
            if capacity.strip() == b["区间"]:
                return b["分数"]
        return 0

    def calc_battery_density_score(self, density):
        for b in self.battery_density:
            if density.strip() == b["区间"]:
                return b["分数"]
        return 0

    def calc_wired_charging_score(self, power):
        for w in self.wired_charging:
            if power.strip() == w["区间"]:
                return w["分数"]
        return 0

    def calc_wireless_charging_score(self, power):
        for w in self.wireless_charging:
            if power.strip() == w["区间"]:
                return w["分数"]
        return 0

    def calc_reverse_wireless_charging_score(self, power):
        for w in self.reverse_wireless_charging:
            if power.strip() == w["区间"]:
                return w["分数"]
        return 0

    # 机身结构打分方法
    def calc_frame_material_score(self, material):
        for f in self.frame_materials:
            if material.strip() == f["材质"]:
                return f["分数"]
        return 0

    def calc_device_weight_score(self, weight):
        for w in self.device_weight:
            if weight.strip() == w["区间"]:
                return w["分数"]
        return 0

    def calc_ip_rating_score(self, rating):
        for i in self.ip_rating:
            if rating.strip() == i["等级"]:
                return i["分数"]
        return 0

    def calc_vc_heat_pipe_score(self, area):
        for v in self.vc_heat_pipe:
            if area.strip() == v["区间"]:
                return v["分数"]
        return 0

    def calc_graphene_cooling_score(self, cooling_type):
        for g in self.graphene_cooling:
            if cooling_type.strip() == g["类型"]:
                return g["分数"]
        return 0

    # 通信模块打分方法
    def calc_wifi_score(self, version):
        for w in self.wifi_modules:
            if version.strip() == w["版本"]:
                return w["分数"]
        return 0

    def calc_bluetooth_score(self, version):
        for b in self.bluetooth_modules:
            if version.strip() == b["版本"]:
                return b["分数"]
        return 0

    # 其他硬件打分方法
    def calc_usb_c_score(self, protocol):
        for u in self.usb_c_interfaces:
            if protocol.strip() == u["协议"]:
                return u["分数"]
        return 0

    def calc_usb_video_score(self, protocol):
        for u in self.usb_video_output:
            if protocol.strip() == u["协议"]:
                return u["分数"]
        return 0

    def calc_sim_slot_score(self, scheme):
        for s in self.sim_slots:
            if scheme.strip() == s["方案"]:
                return s["分数"]
        return 0

    def calc_speaker_score(self, scheme):
        for s in self.speakers:
            if scheme.strip() == s["方案"]:
                return s["分数"]
        return 0

    # 修复2: calc_simple_score - 正确处理count类型
    def calc_simple_score(self, hardware_item, user_value):
        """根据简单计分规则计算分数
        hardware_item: 硬件项名称
        user_value: 用户输入的值
          - has类型: "有" 或 "无"
          - select类型: 选项值（如"蓝宝石"）
          - count类型: 数字（用户填的个数，直接当分数）
        """
        # 先查找count类型（用户输入的数字就是分数）
        for s in self.simple_scoring:
            if s["硬件项"] == hardware_item and s["类型"] == "count":
                try:
                    return "count", int(user_value)
                except (ValueError, TypeError):
                    return "not_found", 0

        # 再查找has/select类型（匹配规则字段）
        for s in self.simple_scoring:
            if s["硬件项"] == hardware_item and s["类型"] in ("has", "select"):
                if str(s["规则"]) == str(user_value):
                    return "ok", s["分数"]
        return "not_found", 0

    def calculate_total_score_detailed(self, selections):
        """计算总分（结构化返回）
        返回:
        {
            "total": int,                    # 硬件总分
            "system_scores": {系统名: 分数},   # 各系统总分
            "details": [                     # 每个硬件项明细
                {
                    "system": "一、核心计算单元",
                    "item": "SoC",
                    "value": "骁龙 8 Elite Gen 5",
                    "score": 85,
                },
                ...
            ],
        }
        """
        total = 0
        system_scores = {}
        details = []
        for system in self.get_categories():
            system_scores[system] = 0

        def add(system, item, value, score):
            nonlocal total
            total += score
            system_scores[system] = system_scores.get(system, 0) + score
            details.append({
                "system": system,
                "item": item,
                "value": value,
                "score": score,
            })

        # ========== 一、核心计算单元 ==========
        if "soc" in selections:
            score = self.calc_soc_score(selections["soc"])
            add("一、核心计算单元", "SoC", selections["soc"], score)

        if "ram" in selections:
            score = self.calc_ram_score(selections["ram"])
            add("一、核心计算单元", "RAM", selections["ram"], score)

        if "ram_capacity" in selections:
            score = self.calc_ram_capacity_score(selections["ram_capacity"])
            add("一、核心计算单元", "RAM容量", f"{selections['ram_capacity']}GB", score)
            
        if "rom" in selections:
            score = self.calc_rom_score(selections["rom"])
            add("一、核心计算单元", "ROM", selections["rom"], score)

        if "capacity" in selections:
            score = self.calc_capacity_score(selections["capacity"])
            add("一、核心计算单元", "存储容量", selections["capacity"], score)

        if "expand_storage" in selections:
            es = selections["expand_storage"]
            card_type = es.get("card_type", "TF卡")
            capacity_gb = es.get("capacity_gb", 0)
            score = self.calc_expand_storage_score(card_type, capacity_gb)
            add("一、核心计算单元", "扩展存储", f"{card_type} {capacity_gb}GB", score)

        # ========== 二、显示系统 ==========
        if "panel_type" in selections:
            score = self.calc_panel_score(selections["panel_type"])
            add("二、显示系统", "面板类型", selections["panel_type"], score)

        if "resolution" in selections:
            score = self.calc_resolution_score(selections["resolution"])
            add("二、显示系统", "分辨率", selections["resolution"], score)

        if "refresh_rate" in selections:
            score = self.calc_refresh_rate_score(selections["refresh_rate"])
            add("二、显示系统", "刷新率", selections["refresh_rate"], score)

        if "touch_sampling_cont" in selections:
            score = self.calc_touch_sampling_cont_score(selections["touch_sampling_cont"])
            add("二、显示系统", "持续触控采样率", selections["touch_sampling_cont"], score)

        if "touch_sampling_peak" in selections:
            score = self.calc_touch_sampling_peak_score(selections["touch_sampling_peak"])
            add("二、显示系统", "峰值触控采样率", selections["touch_sampling_peak"], score)

        if "brightness_manual" in selections:
            score = self.calc_brightness_manual_score(selections["brightness_manual"])
            add("二、显示系统", "手动最大亮度", selections["brightness_manual"], score)

        if "brightness_local_peak" in selections:
            score = self.calc_brightness_local_peak_score(selections["brightness_local_peak"])
            add("二、显示系统", "局部峰值亮度", selections["brightness_local_peak"], score)

        if "brightness_hbm" in selections:
            score = self.calc_brightness_hbm_score(selections["brightness_hbm"])
            add("二、显示系统", "HBM全屏激发亮度", selections["brightness_hbm"], score)

        # ========== 三、影像系统 ==========
        # 主摄
        if "main_sensor_size" in selections:
            score = self.calc_main_sensor_size_score(selections["main_sensor_size"])
            add("三、影像系统", "主摄传感器尺寸", selections["main_sensor_size"], score)

        if "main_pixel" in selections:
            score = self.calc_main_pixel_score(selections["main_pixel"])
            add("三、影像系统", "主摄像素", selections["main_pixel"], score)

        if "main_aperture" in selections:
            score = self.calc_main_aperture_score(selections["main_aperture"])
            add("三、影像系统", "主摄光圈", selections["main_aperture"], score)

        if "main_ois" in selections:
            score = self.calc_main_ois_score(selections["main_ois"])
            add("三、影像系统", "主摄OIS", selections["main_ois"], score)

        # 超广角
        if "ultra_sensor_size" in selections:
            score = self.calc_ultra_sensor_size_score(selections["ultra_sensor_size"])
            add("三、影像系统", "超广角传感器尺寸", selections["ultra_sensor_size"], score)

        if "ultra_fov" in selections:
            score = self.calc_ultra_fov_score(selections["ultra_fov"])
            add("三、影像系统", "超广角视角", selections["ultra_fov"], score)

        if "ultra_pixel" in selections:
            score = self.calc_ultra_pixel_score(selections["ultra_pixel"])
            add("三、影像系统", "超广角像素", selections["ultra_pixel"], score)

        if "ultra_aperture" in selections:
            score = self.calc_ultra_aperture_score(selections["ultra_aperture"])
            add("三、影像系统", "超广角光圈", selections["ultra_aperture"], score)

        if "ultra_ois" in selections:
            score = self.calc_ultra_ois_score(selections["ultra_ois"])
            add("三、影像系统", "超广角OIS", selections["ultra_ois"], score)

        # 长焦
        if "tele_pixel" in selections:
            score = self.calc_tele_pixel_score(selections["tele_pixel"])
            add("三、影像系统", "长焦像素", selections["tele_pixel"], score)

        if "tele_zoom" in selections:
            score = self.calc_tele_zoom_score(selections["tele_zoom"])
            add("三、影像系统", "长焦变焦", selections["tele_zoom"], score)

        if "tele_sensor_size" in selections:
            score = self.calc_tele_sensor_size_score(selections["tele_sensor_size"])
            add("三、影像系统", "长焦传感器尺寸", selections["tele_sensor_size"], score)

        if "tele_ois" in selections:
            score = self.calc_tele_ois_score(selections["tele_ois"])
            add("三、影像系统", "长焦OIS", selections["tele_ois"], score)

        # 前置
        if "front_wide_pixel" in selections:
            score = self.calc_front_wide_pixel_score(selections["front_wide_pixel"])
            add("三、影像系统", "前置广角像素", selections["front_wide_pixel"], score)

        if "front_fov" in selections:
            score = self.calc_front_fov_score(selections["front_fov"])
            add("三、影像系统", "前置视角", selections["front_fov"], score)

        if "front_sensor_size" in selections:
            score = self.calc_front_sensor_size_score(selections["front_sensor_size"])
            add("三、影像系统", "前置传感器尺寸", selections["front_sensor_size"], score)

        if "front_pixel" in selections:
            score = self.calc_front_pixel_score(selections["front_pixel"])
            add("三、影像系统", "前置像素", selections["front_pixel"], score)

        # ========== 四、能源系统 ==========
        if "battery_capacity" in selections:
            score = self.calc_battery_capacity_score(selections["battery_capacity"])
            add("四、能源系统", "电池容量", selections["battery_capacity"], score)

        if "battery_density" in selections:
            score = self.calc_battery_density_score(selections["battery_density"])
            add("四、能源系统", "电池能量密度", selections["battery_density"], score)

        if "wired_charging" in selections:
            score = self.calc_wired_charging_score(selections["wired_charging"])
            add("四、能源系统", "有线充电", selections["wired_charging"], score)

        if "wireless_charging" in selections:
            score = self.calc_wireless_charging_score(selections["wireless_charging"])
            add("四、能源系统", "无线充电", selections["wireless_charging"], score)

        if "reverse_wireless_charging" in selections:
            score = self.calc_reverse_wireless_charging_score(selections["reverse_wireless_charging"])
            add("四、能源系统", "反向无线充电", selections["reverse_wireless_charging"], score)

        # ========== 五、机身结构 ==========
        if "frame_material" in selections:
            score = self.calc_frame_material_score(selections["frame_material"])
            add("五、机身结构", "中框材质", selections["frame_material"], score)

        if "device_weight" in selections:
            score = self.calc_device_weight_score(selections["device_weight"])
            add("五、机身结构", "机身重量", selections["device_weight"], score)

        if "ip_rating" in selections:
            score = self.calc_ip_rating_score(selections["ip_rating"])
            add("五、机身结构", "IP防护等级", selections["ip_rating"], score)

        if "vc_heat_pipe" in selections:
            score = self.calc_vc_heat_pipe_score(selections["vc_heat_pipe"])
            add("五、机身结构", "VC均热板", selections["vc_heat_pipe"], score)

        if "graphene_cooling" in selections:
            score = self.calc_graphene_cooling_score(selections["graphene_cooling"])
            add("五、机身结构", "石墨烯散热", selections["graphene_cooling"], score)

        # ========== 六、通信模块 ==========
        if "wifi" in selections:
            score = self.calc_wifi_score(selections["wifi"])
            add("六、通信模块", "WiFi", selections["wifi"], score)

        if "bluetooth" in selections:
            score = self.calc_bluetooth_score(selections["bluetooth"])
            add("六、通信模块", "蓝牙", selections["bluetooth"], score)

        # ========== 八、其他硬件 ==========
        if "usb_c" in selections:
            score = self.calc_usb_c_score(selections["usb_c"])
            add("八、其他硬件", "USB接口", selections["usb_c"], score)

        if "usb_video" in selections:
            score = self.calc_usb_video_score(selections["usb_video"])
            add("八、其他硬件", "USB视频输出", selections["usb_video"], score)

        if "sim_slot" in selections:
            score = self.calc_sim_slot_score(selections["sim_slot"])
            add("八、其他硬件", "SIM卡槽", selections["sim_slot"], score)

        if "speaker" in selections:
            score = self.calc_speaker_score(selections["speaker"])
            add("八、其他硬件", "扬声器", selections["speaker"], score)

        # ========== 简单计分（系统归属从 SIMPLE_SCORING 读取） ==========
        if "simple" in selections:
            for rule_name, rule_value in selections["simple"].items():
                result, score = self.calc_simple_score(rule_name, rule_value)
                if result in ("ok", "count"):
                    system = "八、其他硬件"
                    for s in self.simple_scoring:
                        if s["硬件项"] == rule_name:
                            system = s["大类"]
                            break
                    add(system, rule_name, rule_value, score)

        return {
            "total": total,
            "system_scores": system_scores,
            "details": details,
        }

# ==================== 测试 ====================
if __name__ == "__main__":
    engine = ScoringEngine()

    def title(text):
        print(f"\n{'=' * 50}")
        print(text)
        print('=' * 50)

    # ==================== 一、单项打分测试 ====================
    title("单项打分测试")

    print("[SoC]")
    for chip in ["骁龙 8 Elite Gen 5", "天玑 9400", "Apple A19 Pro", "骁龙 870", "麒麟 980"]:
        print(f"  {chip} => {engine.calc_soc_score(chip)}分")

    print("\n[RAM]")
    for ram in ["LPDDR6", "LPDDR5X Ultra", "LPDDR5T", "LPDDR4X"]:
        print(f"  {ram} => {engine.calc_ram_score(ram)}分")

    print("\n[存储容量]")
    for cap in [64, 128, 256, 512, 1024]:
        print(f"  {cap}GB => {engine.calc_capacity_score(cap)}分")

    print("\n[扩展存储]")
    tf = engine.calc_expand_storage_score("TF卡", 512)
    nm = engine.calc_expand_storage_score("华为NM卡", 512)
    print(f"  TF卡 512GB => {tf}分")
    print(f"  华为NM卡 512GB => {nm}分（比TF卡多{nm - tf}分）")

    print("\n[显示面板]")
    for panel in ["双层OLED", "单层OLED", "AMOLED", "LCD"]:
        print(f"  {panel} => {engine.calc_panel_score(panel)}分")

    print("\n[USB视频输出]")
    for proto in ["DP 1.2 Alt Mode", "DP 1.4 Alt Mode", "DP 2.1 Alt Mode"]:
        print(f"  {proto} => {engine.calc_usb_video_score(proto)}分")

    print("\n[简单计分]")
    for item, val in [
        ("充电协议", 3),          # count
        ("频段支持", 5),          # count
        ("影像协处理器", "有"),    # has
        ("疏油层", "纳米级疏油层"),  # select
        ("背板材质", "特殊材质"),   # select
    ]:
        result, score = engine.calc_simple_score(item, val)
        print(f"  {item}={val} => 类型={result}, 分数={score}")

    # ==================== 二、总分测试 ====================
    title("总分测试")

    mock_selections = {
        "soc": "天玑 9400",
        "ram": "LPDDR5X Ultra",
        "rom": "UFS 4.0",
        "capacity": 512,
        "expand_storage": {"card_type": "华为NM卡", "capacity_gb": 512},
        "panel_type": "单层OLED",
        "resolution": "FHD+",
        "refresh_rate": "120Hz",
        "touch_sampling_cont": "720Hz",
        "touch_sampling_peak": "3000Hz",
        "brightness_manual": "1000-1200nit",
        "brightness_local_peak": "4500-5000nit",
        "brightness_hbm": "1000-1200nit",
        "main_sensor_size": "1英寸（1/0.98英寸）",
        "main_pixel": "2亿（200MP）",
        "main_aperture": "f/1.4",
        "main_ois": "CIPA 7.5",
        "ultra_sensor_size": "1/1.28英寸",
        "ultra_fov": "123°",
        "ultra_pixel": "5000万（50MP）原生像素",
        "ultra_aperture": "f/1.6",
        "ultra_ois": "CIPA 7.5",
        "tele_pixel": "2亿（200MP）",
        "tele_zoom": "10倍",
        "tele_sensor_size": "1/1.28英寸",
        "tele_ois": "CIPA 7.5",
        "front_wide_pixel": "2亿（200MP）",
        "front_fov": "110°",
        "front_sensor_size": "1/2.0英寸",
        "front_pixel": "2亿（200MP）",
        "battery_capacity": "≥10000mAh",
        "battery_density": "≥950 Wh/L",
        "wired_charging": "≥200W",
        "wireless_charging": "≥80W",
        "reverse_wireless_charging": "≥20W",
        "frame_material": "钛合金（Grade 5/TC4）",
        "device_weight": "≤165g",
        "ip_rating": "IP68",
        "vc_heat_pipe": "≥15000mm²",
        "graphene_cooling": "单层超高导热石墨烯膜",
        "wifi": "Wi-Fi 7(802.11be)",
        "bluetooth": "蓝牙 6.0",
        "usb_c": "USB4 Gen 3×2",
        "usb_video": "DP 2.1 Alt Mode",
        "sim_slot": "双Nano-SIM + 双eSIM",
        "speaker": "2.1声道系统（对称双扬+独立低音炮）",
        "simple": {
            "影像协处理器": "有",
            "AI协处理器": "有",
            "安全协处理器": "有",
            "游戏独显芯片": "有",
            "触控IC": "有",
            "背板材质": "特殊材质",
            "疏油层": "纳米级疏油层",
            "充电协议": 3,
            "频段支持": 5,
            "GPS/GNSS": 3,
            "麦克风阵列": 4,
            "光线传感器": "有",
            "气压计": "有",
            "陀螺仪": "有",
            "加速度传感器": "有",
            "指南针/电子罗盘": "有",
            "指纹传感器类型": "超声波",
            "红外传感器": "有",
            "霍尔传感器": "有",
            "距离传感器": "有",
        },
    }

    result = engine.calculate_total_score_detailed(mock_selections)

    print(f"硬件总分: {result['total']}分")
    print(f"系统数量: {len(result['system_scores'])}")
    print(f"明细项数: {len(result['details'])}")

    # ==================== 三、一致性校验 ====================
    title("一致性校验")

    total_from_details = sum(d["score"] for d in result["details"])
    total_from_systems = sum(result["system_scores"].values())

    ok1 = "✓" if total_from_details == result["total"] else "✗"
    ok2 = "✓" if total_from_systems == result["total"] else "✗"

    print(f"  total 字段      : {result['total']}")
    print(f"  明细求和        : {total_from_details}  {ok1}")
    print(f"  系统求和        : {total_from_systems}  {ok2}")

    # 检查是否有重复硬件项
    items = [d["item"] for d in result["details"]]
    duplicates = [x for x in items if items.count(x) > 1]
    if duplicates:
        print(f"  ⚠ 发现重复项    : {set(duplicates)}")
    else:
        print(f"  重复项检查      : 无 ✓")

    # ==================== 四、各系统汇总 ====================
    title("各系统汇总")

    grouped = {}
    for d in result["details"]:
        grouped.setdefault(d["system"], []).append(d)

    for system in engine.get_categories():
        items = grouped.get(system, [])
        system_total = result["system_scores"].get(system, 0)
        print(f"\n【{system}】 系统总分: {system_total}分")
        if not items:
            print("  （无数据）")
            continue
        for d in items:
            print(f"  - {d['item']} = {d['value']} => {d['score']}分")
    title("测试完成")   
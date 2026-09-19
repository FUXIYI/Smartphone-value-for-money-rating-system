# ==================== phone_db.py ====================
# 机型 → 硬件配置库
# 原则：
#   1. 官网明确给出 → 填，字符串与 scoring_engine.py 保持一致
#   2. 官网没给 → 跳过，绝不虚构
#   3. count 类型（频段/GPS/麦克风/充电兼容档位）按"档位数量"填

PHONE_CONFIGS = {

    # ==================== 华为 Mate 80 Pro Max ====================
    "HUAWEI Mate 80 Pro Max": {
        "soc": "麒麟 9030 Pro",
        "ram_capacity": 16,
        "capacity": 512,
        "expand_storage": {"card_type": "无", "capacity_gb": 0},

        "panel_type": "双层OLED",
        "resolution": "FHD+",
        "refresh_rate": "120Hz",
        "touch_sampling_cont": "300Hz",

        "main_pixel": "5000万（50MP）",
        "main_aperture": "f/1.4",
        "ultra_pixel": "4000万（40MP）",
        "ultra_aperture": "f/2.2",
        "tele_pixel": "5000万（50MP）",
        "tele_zoom": "6.2倍",
        "front_wide_pixel": "1300万（13MP）",
        "front_pixel": "1300万（13MP）",

        "battery_capacity": "5500~6999mAh",
        "wired_charging": "100~149W",
        "wireless_charging": "≥80W",
        "device_weight": "236~260g",
        "ip_rating": "IP68+IP69",

        "wifi": "Wi-Fi 7(802.11be)",
        "bluetooth": "蓝牙 6.0",
        "usb_c": "USB 3.2 Gen 1×1",
        "sim_slot": "双Nano-SIM（传统双卡槽）",

        "simple": {
            "3D结构光模块": "有",
            "深感摄像头": "有",
            "盖板材质": "有强化玻璃",
            "激光对焦传感器": "有",
            "色温传感器": "有",
            "自动对焦（AF）": "有",
            "闪光灯": "有",
            "OIS光学防抖马达": "有",
            "NFC芯片": "有",
            "红外遥控": "有",
            "星闪模块": "有",
            "天通卫星芯片": "有",
            "北斗卫星芯片": "有",
            "卫星通话/短信": "有",
            "光线传感器": "有",
            "气压计": "有",
            "陀螺仪": "有",
            "加速度传感器": "有",
            "指南针/电子罗盘": "有",
            "指纹传感器类型": "侧边电容",
            "红外传感器": "有",
            "霍尔传感器": "有",
            "距离传感器": "有",
            "充电兼容档位": 8,           # 20V/5A、20V/4.4A、11V/6A、10V/4A、10V/2.25A、4.5V/5A、5V/4.5A、9V/2A
            "GPS/GNSS": 13,              # GPS(L1+L5)+GLONASS+北斗(B1I+B1C+B2a+B2b)+GALILEO(E1+E5a+E5b)+QZSS(L1+L5)+NavIC
            # 频段支持：官网未列具体数量 → 跳过
        },
    },

    # ==================== Xiaomi 17 Ultra 徕卡版 ====================
    "Xiaomi 17 Ultra 徕卡版": {
        "soc": "骁龙 8 Elite Gen 5",
        "ram": "LPDDR5X（标准）",
        "ram_capacity": 16,
        "rom": "UFS 4.1",
        "capacity": 512,
        "expand_storage": {"card_type": "无", "capacity_gb": 0},

        "panel_type": "AMOLED",
        "resolution": "1.5K",
        "refresh_rate": "120Hz",
        "touch_sampling_cont": "300Hz",
        "brightness_local_peak": "3200-4000nit",

        "main_sensor_size": "1英寸（1/0.98英寸）",
        "main_pixel": "5000万（50MP）",
        "main_aperture": "f/1.67",
        "ultra_fov": "115°",
        "ultra_pixel": "5000万（50MP）原生像素",
        "ultra_aperture": "f/2.2",
        "tele_pixel": "2亿（200MP）",
        "tele_zoom": "4.3倍",
        "tele_sensor_size": "1/1.4英寸",
        "front_wide_pixel": "5000万（50MP）",
        "front_fov": "90°",
        "front_pixel": "5000万（50MP）",

        "battery_capacity": "5500~6999mAh",
        "wired_charging": "80~99W",
        "wireless_charging": "50~79W",
        "reverse_wireless_charging": "≥20W",
        "device_weight": "216~235g",
        "ip_rating": "IP68+IP69",

        "wifi": "Wi-Fi 7(802.11be)",
        "bluetooth": "蓝牙 5.4",
        "usb_c": "USB 3.2 Gen 2×1",
        "sim_slot": "双Nano-SIM（传统双卡槽）",

        "simple": {
            "盖板材质": "有强化玻璃",
            "物理变焦环": "有",
            "色彩摄像头": "有",
            "激光对焦传感器": "有",
            "色温传感器": "有",
            "Flicker传感器": "有",
            "多光谱传感器": "有",
            "自动对焦/微距": "有",
            "自动对焦（AF）": "有",
            "闪光灯": "有",
            "OIS光学防抖马达": "有",
            "NFC芯片": "有",
            "红外遥控": "有",
            "天通卫星芯片": "有",
            "北斗卫星芯片": "有",
            "卫星通话/短信": "有",
            "光线传感器": "有",
            "气压计": "有",
            "陀螺仪": "有",
            "加速度传感器": "有",
            "指南针/电子罗盘": "有",
            "指纹传感器类型": "超声波",
            "霍尔传感器": "有",
            "距离传感器": "有",
            "频段支持": 27,
            "充电兼容档位": 6,           # QC3+/QC3.0/QC2.0/PD3.0/PD2.0/PPS
            "GPS/GNSS": 11,              # 北斗3+GPS2+Galileo2+GLONASS1+QZSS2+NavIC1
        },
    },

    # ==================== OPPO Find X9 Ultra ====================
    "OPPO Find X9 Ultra": {
        "soc": "骁龙 8 Elite Gen 5",
        "ram": "LPDDR5X（标准）",
        "ram_capacity": 16,
        "rom": "UFS 4.1",
        "capacity": 512,
        "expand_storage": {"card_type": "无", "capacity_gb": 0},

        "panel_type": "AMOLED",
        "resolution": "QHD+ / 2K+",
        "refresh_rate": "144Hz",
        "touch_sampling_cont": "300Hz",
        "brightness_local_peak": "1500-2000nit",

        "main_pixel": "2亿（200MP）",
        "main_aperture": "f/1.5",
        "ultra_fov": "123°",
        "ultra_pixel": "5000万（50MP）原生像素",
        "ultra_aperture": "f/2.0",
        "tele_pixel": "2亿（200MP）",
        "tele_zoom": "10倍",
        "front_wide_pixel": "5000万（50MP）",
        "front_pixel": "5000万（50MP）",

        "battery_capacity": "7000~7999mAh",
        "wired_charging": "100~149W",
        "wireless_charging": "50~79W",
        "device_weight": "236~260g",

        "wifi": "Wi-Fi 7(802.11be)",
        "bluetooth": "蓝牙 6.0",
        "usb_c": "USB 3.2 Gen 1×1",
        "sim_slot": "双Nano-SIM（传统双卡槽）",

        "simple": {
            "自动对焦/微距": "有",
            "自动对焦（AF）": "有",
            "色彩摄像头": "有",
            "激光对焦传感器": "有",
            "色温传感器": "有",
            "多光谱传感器": "有",
            "OIS光学防抖马达": "有",
            "射频增强芯片": "有",
            "NFC芯片": "有",
            "红外遥控": "有",
            "光线传感器": "有",
            "陀螺仪": "有",
            "加速度传感器": "有",
            "指南针/电子罗盘": "有",
            "指纹传感器类型": "超声波",
            "霍尔传感器": "有",
            "距离传感器": "有",
            "ppi": ">450",
            "频段支持": 25,
            "充电兼容档位": 9,           # 100W SCP/100W UFCS/80W SCP/50W SCP/33W SCP/44W UFCS/18W PD/18W QC/55W PPS
            "GPS/GNSS": 10,              # 北斗3+GPS2+GLONASS1+Galileo2+QZSS2
        },
    },

    # ==================== vivo X300 Ultra ====================
    "vivo X300 Ultra": {
        "soc": "骁龙 8 Elite Gen 5",
        "ram": "LPDDR5X Ultra",
        "ram_capacity": 16,
        "rom": "UFS 4.1",
        "capacity": 512,

        "panel_type": "AMOLED",
        "resolution": "QHD+ / 2K+",
        "refresh_rate": "144Hz",

        "main_pixel": "2亿（200MP）",
        "main_aperture": "f/1.85",
        "ultra_pixel": "5000万（50MP）原生像素",
        "ultra_aperture": "f/2.0",
        "tele_pixel": "2亿（200MP）",
        "tele_zoom": "3.7倍",
        "front_wide_pixel": "5000万（50MP）",
        "front_pixel": "5000万（50MP）",

        "battery_capacity": "5500~6999mAh",
        "wired_charging": "100~149W",
        "wireless_charging": "30~49W",
        "device_weight": "236~260g",

        "wifi": "Wi-Fi 7(802.11be)",
        "bluetooth": "蓝牙 5.4",
        "usb_c": "USB 3.2 Gen 1×1",
        "usb_video": "DP 1.4 Alt Mode",
        "sim_slot": "双Nano-SIM（传统双卡槽）",

        "simple": {
            "自动对焦（AF）": "有",
            "激光对焦传感器": "有",
            "色温传感器": "有",
            "Flicker传感器": "有",
            "OIS光学防抖马达": "有",
            "NFC芯片": "有",
            "红外遥控": "有",
            "北斗卫星芯片": "有",
            "卫星通话/短信": "有",
            "光线传感器": "有",
            "陀螺仪": "有",
            "加速度传感器": "有",
            "指南针/电子罗盘": "有",
            "指纹传感器类型": "超声波",
            "霍尔传感器": "有",
            "距离传感器": "有",
            "ppi": ">450",
            "频段支持": 25,
            "充电兼容档位": 1,           # 官网只写 100W 有线，未列具体档位
            "GPS/GNSS": 10,              # 北斗3+GPS2+GLONASS1+Galileo2+QZSS2
        },
    },

    # ==================== iQOO 15 Ultra ====================
    "iQOO 15 Ultra": {
        "soc": "骁龙 8 Elite Gen 5",
        "ram": "LPDDR5X Ultra Pro",
        "ram_capacity": 24,
        "rom": "UFS 4.1",
        "capacity": 512,
        "expand_storage": {"card_type": "无", "capacity_gb": 0},

        "panel_type": "AMOLED",
        "resolution": "QHD+ / 2K+",
        "refresh_rate": "144Hz",

        "main_pixel": "5000万（50MP）",
        "main_aperture": "f/1.88",
        "ultra_pixel": "5000万（50MP）原生像素",
        "ultra_aperture": "f/2.05",
        "tele_pixel": "5000万（50MP）",
        "front_wide_pixel": "3200万（32MP）",
        "front_pixel": "3200万（32MP）",

        "battery_capacity": "7000~7999mAh",
        "wired_charging": "100~149W",
        "wireless_charging": "30~49W",
        "device_weight": "216~235g",

        "wifi": "Wi-Fi 7(802.11be)",
        "bluetooth": "蓝牙 6.0",
        "usb_c": "USB 3.2 Gen 1×1",
        "sim_slot": "双Nano-SIM（传统双卡槽）",

        "simple": {
            "自动对焦（AF）": "有",
            "色温传感器": "有",
            "Flicker传感器": "有",
            "OIS光学防抖马达": "有",
            "NFC芯片": "有",
            "红外遥控": "有",
            "光线传感器": "有",
            "陀螺仪": "有",
            "加速度传感器": "有",
            "指南针/电子罗盘": "有",
            "指纹传感器类型": "超声波",
            "霍尔传感器": "有",
            "距离传感器": "有",
            "ppi": ">450",
            "频段支持": 31,
            "充电兼容档位": 10,          # 11V/9.1A~5V/2A 共 10 档
            "GPS/GNSS": 10,
        },
    },

    # ==================== 一加 15 ====================
    "一加 15": {
        "soc": "骁龙 8 Elite Gen 5",
        "ram": "LPDDR5X（标准）",
        "ram_capacity": 16,
        "rom": "UFS 4.1",
        "capacity": 512,

        "resolution": "FHD+",
        "refresh_rate": "120Hz",
        "brightness_local_peak": "1500-2000nit",

        "main_pixel": "5000万（50MP）",
        "main_aperture": "f/1.8",
        "ultra_fov": "116°",
        "ultra_pixel": "5000万（50MP）原生像素",
        "ultra_aperture": "f/2.0",
        "tele_pixel": "5000万（50MP）",
        "tele_zoom": "3.5倍",
        "front_wide_pixel": "3200万（32MP）",
        "front_pixel": "3200万（32MP）",

        "battery_capacity": "7000~7999mAh",
        "wired_charging": "100~149W",
        "wireless_charging": "50~79W",
        "device_weight": "196~215g",
        "ip_rating": "IP68+IP69+IP69K",
        "speaker": "超导磁线性立体声双扬声器",

        "wifi": "Wi-Fi 7(802.11be)",
        "bluetooth": "蓝牙 6.0",
        "usb_c": "USB 3.2 Gen 1×1",
        "sim_slot": "双Nano-SIM（传统双卡槽）",

        "simple": {
            "自动对焦（AF）": "有",
            "盖板材质": "有强化玻璃",
            "激光对焦传感器": "有",
            "色温传感器": "有",
            "多光谱传感器": "有",
            "OIS光学防抖马达": "有",
            "NFC芯片": "有",
            "红外遥控": "有",
            "光线传感器": "有",
            "陀螺仪": "有",
            "加速度传感器": "有",
            "指南针/电子罗盘": "有",
            "指纹传感器类型": "超声波",
            "霍尔传感器": "有",
            "距离传感器": "有",
            "麦克风阵列": 3,
            "ppi": "350-450",
            "频段支持": 21,
            "充电兼容档位": 7,           # 120W SCP/120W UFCS/100W SCP/44W UFCS/55W PPS/36W PD/36W QC
            "GPS/GNSS": 10,              # 北斗3+GPS2+GLONASS1+Galileo2+QZSS2
        },
    },

    # ==================== iPhone 17 ====================
    "iPhone 17": {
        "soc": "Apple A19",
        "capacity": 512,

        "panel_type": "单层OLED",
        "resolution": "1.5K",
        "refresh_rate": "120Hz",
        "brightness_local_peak": "2500-3000nit",

        "main_pixel": "4800万（48MP）",
        "main_aperture": "f/1.6",
        "ultra_fov": "120°",
        "ultra_pixel": "4800万（48MP）原生像素",
        "ultra_aperture": "f/2.2",
        "tele_zoom": "2倍",
        "front_wide_pixel": "1800万（18MP）",
        "front_pixel": "1800万（18MP）",

        "wired_charging": "≤40W",
        "wireless_charging": "≤15W",
        "device_weight": "166~180g",
        "ip_rating": "IP68",

        "wifi": "Wi-Fi 7(802.11be)",
        "bluetooth": "蓝牙 6.0",
        "usb_c": "USB 2.0",
        "sim_slot": "双Nano-SIM（传统双卡槽）",

        "simple": {
            "3D结构光模块": "有",
            "深感摄像头": "有",
            "盖板材质": "有强化玻璃",
            "自动对焦/微距": "有",
            "自动对焦（AF）": "有",
            "OIS光学防抖马达": "有",
            "NFC芯片": "有",
            "光线传感器": "有",
            "气压计": "有",
            "陀螺仪": "有",
            "加速度传感器": "有",
            "指南针/电子罗盘": "有",
            "距离传感器": "有",
            "ppi": ">450",
            "频段支持": 22,              # FDD-5G NR 15 + TDD-5G NR 7
            "充电兼容档位": 1,           # 官网只列 40W PD
            "GPS/GNSS": 7,               # GPS(L1+L5)+GLONASS+Galileo+QZSS+北斗+NavIC
        },
    },

    # ==================== 荣耀 Magic8 RSR 保时捷设计 ====================
    "荣耀 Magic8 RSR 保时捷设计": {
        "soc": "骁龙 8 Elite Gen 5",
        "ram_capacity": 24,
        "capacity": 512,
        "expand_storage": {"card_type": "无", "capacity_gb": 0},

        "panel_type": "AMOLED",
        "resolution": "FHD+",
        "refresh_rate": "120Hz",
        "brightness_local_peak": "5500-6000nit",   # HDR 峰值 6000nits

        "main_sensor_size": "1/1.3英寸",
        "main_pixel": "5000万（50MP）",
        "main_aperture": "f/1.6",
        "ultra_fov": "122°",
        "ultra_pixel": "5000万（50MP）原生像素",
        "ultra_aperture": "f/2.0",
        "tele_pixel": "2亿（200MP）",
        "tele_zoom": "3.7倍",
        "tele_sensor_size": "1/1.4英寸",
        "front_wide_pixel": "5000万（50MP）",
        "front_fov": "90°",
        "front_pixel": "5000万（50MP）",

        "battery_capacity": "7000~7999mAh",        # 7200mAh
        "wired_charging": "100~149W",              # 120W
        "wireless_charging": "≥80W",               # 80W
        "device_weight": "236~260g",               # 239g
        "ip_rating": "IP68+IP69+IP69K",

        "wifi": "Wi-Fi 7(802.11be)",
        "bluetooth": "蓝牙 6.0",
        "usb_c": "USB 3.2 Gen 1×1",
        "usb_video": "DP 1.2 Alt Mode",
        "sim_slot": "双Nano-SIM（传统双卡槽）",

        "simple": {
            # 影像
            "深感摄像头": "有",
            "激光对焦传感器": "有",
            "色温传感器": "有",
            "Flicker传感器": "有",
            "自动对焦（AF）": "有",
            "闪光灯": "有",
            "OIS光学防抖马达": "有",

            # 通信
            "射频增强芯片": "有",
            "NFC芯片": "有",
            "红外遥控": "有",
            "天通卫星芯片": "有",
            "北斗卫星芯片": "有",
            "卫星通话/短信": "有",

            # 传感器
            "光线传感器": "有",
            "气压计": "有",
            "陀螺仪": "有",
            "加速度传感器": "有",
            "指南针/电子罗盘": "有",
            "红外传感器": "有",
            "霍尔传感器": "有",
            "距离传感器": "有",

            # 显示
            "盖板材质": "有强化玻璃",

            # 音频
            "麦克风阵列": 3,

            # count 类型
            "充电兼容档位": 1,                  # 官网只写 120W 荣耀超级快充
            "GPS/GNSS": 14,                     # 北斗4+GPS2+GLONASS1+Galileo3+QZSS2+NavIC2
            # 频段支持：官网未列具体数量 → 跳过
            # 指纹传感器类型：官网只写"指纹传感器"，未明说 → 跳过
            # speaker：官网只写"立体声扬声器"，未给具体方案 → 跳过
        },
    },
}


# ==================== 对外接口 ====================

def get_all_phones():
    return list(PHONE_CONFIGS.keys())


def get_config(phone_name):
    return PHONE_CONFIGS.get(phone_name.strip())


# ==================== 自测 ====================
if __name__ == "__main__":
    from scoring_engine import ScoringEngine

    engine = ScoringEngine()

    for phone in get_all_phones():
        cfg = get_config(phone)
        result = engine.calculate_total_score_detailed(cfg)

        print(f"\n{'=' * 56}")
        print(f"  {phone}")
        print(f"{'=' * 56}")
        print(f"  硬件总分：{result['total']}")
        print(f"  各系统得分：")
        for sys, s in result["system_scores"].items():
            if s > 0:
                print(f"    {sys}: {s}")

        zeros = [d for d in result["details"] if d["score"] == 0]
        if zeros:
            print(f"  ⚠ 未匹配项：")
            for d in zeros:
                print(f"    [{d['system']}] {d['item']} = {d['value']}")
# ==================== app.py ====================
import json
from pathlib import Path
from flask import Flask, jsonify, request, render_template

from scoring_engine import ScoringEngine
from phone_db import PHONE_CONFIGS as FACTORY_PHONES


app = Flask(__name__)
engine = ScoringEngine()

# 运行时数据文件（和 app.py 同目录）
PHONES_FILE = Path(__file__).parent / "phones.json"


# ==================== 数据层 ====================

def _write_phones(data):
    with open(PHONES_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def _read_phones():
    if not PHONES_FILE.exists():
        # 首次运行：把 phone_db.py 的内容落盘
        _write_phones(FACTORY_PHONES)
        return dict(FACTORY_PHONES)
    with open(PHONES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


# 全局内存副本（本地开发，不涉及并发）
PHONES = _read_phones()


def save_all():
    _write_phones(PHONES)


# ==================== 页面路由 ====================
@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")


@app.route("/score.html")
def score_page():
    return render_template("score.html")


@app.route("/rules.html")
def rules_page():
    return render_template("rules.html")


@app.route("/custom.html")
def custom_page():
    return render_template("custom.html")


# ==================== 接口：机型列表 ====================

@app.route("/api/phones")
def api_phones():
    return jsonify(list(PHONES.keys()))


# ==================== 接口：按机型 + 价格打分 ====================

@app.route("/api/score_by_phone")
def api_score_by_phone():
    phone = request.args.get("phone", "").strip()
    try:
        price = float(request.args.get("price", 0))
    except (ValueError, TypeError):
        return jsonify({"error": "价格必须是数字"}), 400

    if phone not in PHONES:
        return jsonify({"error": f"未收录机型：{phone}"}), 404
    if price <= 0:
        return jsonify({"error": "价格必须大于 0"}), 400

    result = engine.calculate_total_score_detailed(PHONES[phone])
    result["phone"] = phone
    result["price"] = price
    result["性价比分"] = round(result["total"] / price * 1000)
    return jsonify(result)
@app.route("/api/score_custom", methods=["POST"])
def api_score_custom():
    """临时打分（不保存到机型库）"""
    data = request.json or {}
    phone = (data.get("phone") or "自定义机型").strip()
    try:
        price = float(data.get("price") or 0)
    except (ValueError, TypeError):
        return jsonify({"error": "价格必须是数字"}), 400
    config = data.get("config") or {}

    if price <= 0:
        return jsonify({"error": "价格必须大于 0"}), 400
    if not config:
        return jsonify({"error": "缺少硬件配置"}), 400

    result = engine.calculate_total_score_detailed(config)
    result["phone"] = phone
    result["price"] = price
    result["性价比分"] = round(result["total"] / price * 1000)
    return jsonify(result)

# ==================== 接口：打分规则（给 rules.html） ====================

@app.route("/api/rules")
def api_rules():
    return jsonify({
        "categories": engine.get_categories(),

        # 一、核心计算单元
        "soc": engine.get_soc_options(),
        "ram": engine.get_ram_options(),
        "ram_capacity": engine.get_ram_capacity_options(),
        "rom": engine.get_rom_options(),
        "capacity": engine.get_capacity_options(),
        "expand_storage": engine.get_expand_storage_options(),

        # 二、显示系统
        "panel_type": engine.get_panel_options(),
        "resolution": engine.get_resolution_options(),
        "refresh_rate": engine.get_refresh_rate_options(),
        "touch_sampling_cont": engine.get_touch_sampling_cont_options(),
        "touch_sampling_peak": engine.get_touch_sampling_peak_options(),
        "brightness_manual": engine.get_brightness_manual_options(),
        "brightness_local_peak": engine.get_brightness_local_peak_options(),
        "brightness_hbm": engine.get_brightness_hbm_options(),

        # 三、影像系统
        "main_sensor_size": engine.get_main_sensor_size_options(),
        "main_pixel": engine.get_main_pixel_options(),
        "main_aperture": engine.get_main_aperture_options(),
        "main_ois": engine.get_main_ois_options(),
        "ultra_sensor_size": engine.get_ultra_sensor_size_options(),
        "ultra_fov": engine.get_ultra_fov_options(),
        "ultra_pixel": engine.get_ultra_pixel_options(),
        "ultra_aperture": engine.get_ultra_aperture_options(),
        "ultra_ois": engine.get_ultra_ois_options(),
        "tele_pixel": engine.get_tele_pixel_options(),
        "tele_zoom": engine.get_tele_zoom_options(),
        "tele_sensor_size": engine.get_tele_sensor_size_options(),
        "tele_ois": engine.get_tele_ois_options(),
        "front_wide_pixel": engine.get_front_wide_pixel_options(),
        "front_fov": engine.get_front_fov_options(),
        "front_sensor_size": engine.get_front_sensor_size_options(),
        "front_pixel": engine.get_front_pixel_options(),

        # 四、能源系统
        "battery_capacity": engine.get_battery_capacity_options(),
        "battery_density": engine.get_battery_density_options(),
        "wired_charging": engine.get_wired_charging_options(),
        "wireless_charging": engine.get_wireless_charging_options(),
        "reverse_wireless_charging": engine.get_reverse_wireless_charging_options(),

        # 五、机身结构
        "frame_material": engine.get_frame_material_options(),
        "device_weight": engine.get_device_weight_options(),
        "ip_rating": engine.get_ip_rating_options(),
        "vc_heat_pipe": engine.get_vc_heat_pipe_options(),
        "graphene_cooling": engine.get_graphene_cooling_options(),

        # 六、通信模块
        "wifi": engine.get_wifi_options(),
        "bluetooth": engine.get_bluetooth_options(),

        # 八、其他硬件
        "usb_c": engine.get_usb_c_options(),
        "usb_video": engine.get_usb_video_options(),
        "sim_slot": engine.get_sim_slot_options(),
        "speaker": engine.get_speaker_options(),

        # 简单计分
        "simple_scoring": engine.get_simple_scoring_options(),
    })


# ==================== 接口：查看单个机型配置（给 custom.html 编辑用） ====================

@app.route("/api/phone/<path:name>")
def api_phone_detail(name):
    if name not in PHONES:
        return jsonify({"error": f"未收录机型：{name}"}), 404
    return jsonify({"name": name, "config": PHONES[name]})


# ==================== 接口：自定义机型（新增 / 覆盖 / 删除） ====================

@app.route("/api/custom_phone", methods=["POST"])
def api_custom_phone_save():
    """新增或覆盖机型
    请求体：
    {
      "name": "机型名",
      "overwrite": true,      // 可选，已存在时必须传 true
      "config": { ... }        // 硬件配置
    }
    """
    data = request.json or {}
    name = (data.get("name") or "").strip()
    config = data.get("config") or {}
    overwrite = bool(data.get("overwrite"))

    if not name:
        return jsonify({"error": "机型名不能为空"}), 400
    if not config:
        return jsonify({"error": "缺少硬件配置"}), 400
    if name in PHONES and not overwrite:
        return jsonify({"error": f"机型已存在：{name}，如需覆盖请传 overwrite=true"}), 400

    PHONES[name] = config
    save_all()
    return jsonify({"ok": True, "name": name})


@app.route("/api/custom_phone/<path:name>", methods=["DELETE"])
def api_custom_phone_delete(name):
    if name not in PHONES:
        return jsonify({"error": f"机型不存在：{name}"}), 404
    del PHONES[name]
    save_all()
    return jsonify({"ok": True})


# ==================== 接口：恢复出厂数据 ====================

@app.route("/api/reset_phones", methods=["POST"])
def api_reset_phones():
    """把 phones.json 重置为 phone_db.py 里的内容（用户自建机型会丢）"""
    global PHONES
    PHONES = dict(FACTORY_PHONES)
    save_all()
    return jsonify({"ok": True, "count": len(PHONES)})


# ==================== 启动 ====================

if __name__ == "__main__":
    app.run(debug=True, port=5000)
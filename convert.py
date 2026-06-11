import xml.etree.ElementTree as ET
import re

def svg_to_cad_scr(svg_file, scr_file, scale=1.0):
    try:
        tree = ET.parse(svg_file)
        root = tree.getroot()
    except Exception as e:
        print(f"读取SVG文件失败: {e}")
        return

    # 解析SVG路径
    namespaces = {'svg': 'http://www.w3.org/2000/svg'}
    paths = root.findall('.//{http://www.w3.org/2000/svg}path')
    if not paths:
        paths = root.findall('.//path')

    scr_lines = [
        "UNITS 2 4 1 4 0 N",  # 设置CAD十进制单位
        "ZOOM E"
    ]

    for path in paths:
        d = path.attrib.get('d', '')
        if not d:
            continue
        
        # 提取路径中的指令和坐标数字
        tokens = re.findall(r'([MLHVCSQTAZmlhvcsqtaz])|(-?\d+\.?\d*)', d)
        
        points = []
        last_x, last_y = 0.0, 0.0
        
        i = 0
        while i < len(tokens):
            cmd = tokens[i][0]
            if cmd:
                cmd_upper = cmd.upper()
                if cmd_upper == 'M':  # 移动起点
                    if points:
                        write_pline(scr_lines, points, scale)
                        points = []
                    i += 1
                    x = float(tokens[i][1])
                    i += 1
                    y = float(tokens[i][1])
                    if cmd.islower():
                        x += last_x
                        y += last_y
                    points.append((x, y))
                    last_x, last_y = x, y
                elif cmd_upper == 'L':  # 绘制直线
                    i += 1
                    x = float(tokens[i][1])
                    i += 1
                    y = float(tokens[i][1])
                    if cmd.islower():
                        x += last_x
                        y += last_y
                    points.append((x, y))
                    last_x, last_y = x, y
                elif cmd_upper == 'H':  # 水平绘制
                    i += 1
                    x = float(tokens[i][1])
                    if cmd.islower():
                        x += last_x
                    points.append((x, last_y))
                    last_x = x
                elif cmd_upper == 'V':  # 垂直绘制
                    i += 1
                    y = float(tokens[i][1])
                    if cmd.islower():
                        y += last_y
                    points.append((last_x, y))
                    last_y = y
                elif cmd_upper == 'Z':  # 闭合路径
                    if points:
                        points.append(points[0])
                        write_pline(scr_lines, points, scale)
                        points = []
            i += 1
            
        if points:
            write_pline(scr_lines, points, scale)

    scr_lines.append("ZOOM E")
    
    with open(scr_file, 'w', encoding='utf-8') as f:
        f.write("\n".join(scr_lines))
    print(f"成功！已生成适合AutoCAD运行的脚本文件: {scr_file}")

def write_pline(scr_lines, points, scale):
    if len(points) < 2:
        return
    scr_lines.append("PLINE")
    for pt in points:
        # SVG的Y轴向下，CAD的Y轴向上，因此这里将Y坐标取反
        scr_lines.append(f"{pt[0]*scale:.2f},{-pt[1]*scale:.2f}")
    scr_lines.append("")  # 空行用于结束当前PLINE命令

# 调用函数：输入文件名、输出文件名、缩放比例
svg_to_cad_scr("boy.svg", "boy_rose.scr", scale=1.0)
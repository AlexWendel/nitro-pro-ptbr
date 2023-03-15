import shutil
import os
import subprocess
import re
import pathlib

script_template = """
[FILENAMES]
Exe=output/{filename}.mui
SaveAs=output/{filename}.mui
Log=logs/{filename}.mui.log
[COMMANDS]
-addoverwrite     {res_path}
"""

src = ["BIN Files", "RC Files"]
input_dir = "MUI Files"
output_dir = "output"
rc_files_dir = "RC Files"

rh_path = """C:/Users/Alex/Downloads/resource_hacker/ResourceHacker.exe"""

if not os.path.exists(output_dir):
    os.mkdir(output_dir)

for root, dirs, files in os.walk(input_dir):
    for file in files:
        shutil.copy(f"{input_dir}/{file}", f"{output_dir}/{file}")

for root, dirs, files in os.walk(rc_files_dir):
    for file in files:
        rc_file = open(f"{rc_files_dir}/{file}", "r")
        MUI = rc_file.read().splitlines()[4]
        match = re.search(r'"(.*?)"', MUI)

        bin_file = match[0].replace('"', "").replace(chr(0), "")
        bin_src_path = pathlib.Path(f"BIN Files/{bin_file}")
        bin_path = pathlib.Path(f"{bin_file}")
        shutil.copy(bin_src_path, bin_path)
        res_path = "{}/{}".format(output_dir, file.replace(".rc", ".res"))

        compile_cmd = [
            rh_path,
            "-open",
            f"{rc_files_dir}/{file}",
            "-save",
            res_path,
            "-action",
            "compile",
            "-log",
            "CON",
        ]

        compilation = subprocess.Popen(compile_cmd)
        compilation.communicate()

        script_content = script_template.format(
            filename=file.replace(".rc", ""), res_path=res_path
        )
        script_name = file.replace(".rc", ".txt")
        script_path = f"{output_dir}/{script_name}"

        with open(script_path, "w") as f:
            f.write(script_content)

        compile_dll = subprocess.Popen([rh_path, "-script", script_path], shell=True)
        compile_dll.communicate()

        os.remove(res_path)
        os.remove(script_path)
        os.remove(bin_path)

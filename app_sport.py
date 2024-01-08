import os

import gradio as gr
import tempfile
import shutil
from computeData import *


def generate_file(file_obj):
    global tmpdir
    print('临时文件夹地址：{}'.format(tmpdir))
    print('上传文件的地址：{}'.format(file_obj.name))  # 输出上传后的文件在gradio中保存的绝对地址

    dirname, filename = os.path.split(file_obj.name)

    outFileName = f"out_{filename}"
    outFilePath = os.path.join(tmpdir, outFileName)
    os.makedirs(tmpdir, exist_ok=True)

    startComputeXls(file_obj.name, outFilePath)

    # 返回新文件的的地址（注意这里）
    return outFilePath


def main():
    global tmpdir
    os.makedirs('./tmp/', exist_ok=True)
    with gr.Blocks() as demo:
        with gr.Row():
            with tempfile.TemporaryDirectory(dir='./tmp/') as tmpdir:
                # 定义输入和输出
                inputs = gr.components.File(label="上传文件", file_types=["xlsx"])
                outputs = gr.components.File(label="下载文件", file_types=["xlsx"])
        with gr.Row():
            gen_button = gr.Button("计算体侧成绩")
        with gr.Row():
            with gr.Accordion("demo案例"):
                gr.Markdown("<div align='center'> <a href='https://pan.quark.cn/s/16b6619ea924'> 下载demo文件 </a>  </div>")



        gen_button.click(generate_file, inputs=inputs, outputs=outputs)


        # 启动应用程序
        demo.launch(share=False, server_port=6006)


if __name__ == "__main__":
    main()

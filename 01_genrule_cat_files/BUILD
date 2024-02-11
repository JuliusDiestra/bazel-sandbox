
genrule(
    name = "concat_all_files",
    srcs = [
        "//:file_1.txt",
        "//:file_2.txt",
    ],
    outs = ["concatenated.txt"],
    cmd = "cat $(locations //:file_1.txt) $(location //:file_2.txt) > $@",
)


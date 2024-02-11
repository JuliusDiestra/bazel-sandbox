
genrule(
    name = "run_bash",
    srcs = [
        "//:main.cpp"
    ],
    outs = ["main-bin"],
    tools = ["build-code.sh"],
    cmd = "bash $(location build-code.sh) && mv main-bin $@"
)

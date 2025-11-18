from sitegen import get_config

def main():
    config = get_config()

    # preamble = config.preamble.read_text()

    config.output_folder.mkdir(exist_ok=True, parents=True)

    output_file_path = config.output_folder

    config.input_file.with_suffix(".html")



if __name__ == "__main__":
    main()


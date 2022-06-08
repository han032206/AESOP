import argparse
from helper.utils import *
from stanfordcorenlp import StanfordCoreNLP

if __name__ == '__main__':
    # nlp = StanfordCoreNLP('./evaluation/apps/stanford-corenlp-full-2016-10-31', lang='en')
    # print(nlp.parse('This is an example of tokenziation.'))
    # nlp.close()

    parser = argparse.ArgumentParser()
    parser.add_argument("--output_dir", "-o")
    args = parser.parse_args()

    file_path = "demo-input-data.txt"
    spe = stanford_parsetree_extractor()
    src_pure_parses, src_parses = spe.run(file_path)
    src_lines = [line.strip("\n") for line in open(file_path, "r").readlines()]

    level = 3
    print("write diverse source file")
    # generate the future target parses from the frequencies list
    path = "processed-data/repe_statistics"

    output_file = open(f"{args.output_dir}/level{level}_paranmt.source", "w+")
    frequency_lines = open(f"{path}/repe_para_{level}.txt", "r").readlines()
    level_, freq = generate_dict(frequency_lines), generate_counts_dict(frequency_lines)
    for i in range(0, len(src_lines)):
        print(i)
        possible_drawn = step2_rouge(level_, freq, src_lines[i], level)[3]
        for possible in possible_drawn:
            output_file.write(f"{src_lines[i]}<sep>{src_parses[i]}<sep>{possible}\n")














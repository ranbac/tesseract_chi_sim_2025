def split_text_file(input_path, output_path, min_len=10, max_len=55):
    with open(input_path, 'r', encoding='utf-8') as infile, \
         open(output_path, 'w', encoding='utf-8') as outfile:
        
        for line in infile:
            line = line.strip()
            if len(line) < min_len:
                continue  # Bỏ dòng quá ngắn

            i = 0
            while i < len(line):
                chunk = line[i:i+max_len]
                if len(chunk) < min_len:
                    break  # Bỏ đoạn cuối nếu nhỏ hơn 10 ký tự
                outfile.write(chunk + '\n')
                i += max_len

# Gọi hàm với tên file cụ thể
split_text_file('trainingtext.txt', 'optimizedtrainingtext.txt')

from docx import Document
import pandas as pd
from sqlalchemy import create_engine

# Kết nối cơ sở dữ liệu (thay đổi thông tin kết nối theo cơ sở dữ liệu của bạn)
DATABASE_URI = 'sqlite:///your_database.db'  # Thay đổi URI nếu bạn dùng cơ sở dữ liệu khác
engine = create_engine(DATABASE_URI)

# Lấy dữ liệu từ cơ sở dữ liệu
def fetch_data():
    query = """
    SELECT name, dob, birthplace, id_number, phone, email, workplace, projects, publications, courses
    FROM your_table
    WHERE id = 1  # Thay đổi điều kiện theo nhu cầu
    """
    return pd.read_sql(query, engine).iloc[0]  # Lấy dòng đầu tiên trong kết quả

# Điền thông tin vào file Word
def fill_template(template_path, output_path, data):
    doc = Document(template_path)
    
    for paragraph in doc.paragraphs:
        for key, value in data.items():
            placeholder = f'{{{{{key}}}}}'
            if placeholder in paragraph.text:
                paragraph.text = paragraph.text.replace(placeholder, str(value))

    doc.save(output_path)

# Main function
def main():
    # Cập nhật thông tin cơ sở dữ liệu
    data = fetch_data()
    
    # Điền thông tin vào file Word mẫu
    template_path = 'path/to/your_template.docx'
    output_path = 'path/to/your_output.docx'
    fill_template(template_path, output_path, data)
    print(f"Lý lịch khoa học đã được tạo tại {output_path}")

if __name__ == '__main__':
    main()

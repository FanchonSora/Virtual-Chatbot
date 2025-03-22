import speech_recognition as sr
from antlr4 import *
from SchedulerLexer import SchedulerLexer
from SchedulerParser import SchedulerParser

def parse_command(text: str):
    """
    Hàm parse chuỗi text bằng ANTLR,
    trả về cây cú pháp (parse tree).
    """
    input_stream = InputStream(text)
    lexer = SchedulerLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = SchedulerParser(token_stream)
    tree = parser.command()  # Bắt đầu parse theo rule "command"
    return tree

def interpret_command(tree):
    """
    Duyệt cây parse để rút ra ý định (câu lệnh) 
    và xử lý logic. Ở ví dụ này, ta chỉ minh họa 
    việc phát hiện loại lệnh và in ra kết quả.
    """
    # 1) Kiểm tra rule con: setEventCmd, getScheduleCmd, getDateCmd
    rule_name = tree.getChild(0).getRuleIndex()

    # Cách 1: bạn duyệt thủ công (duyệt node con)
    # Cách 2: dùng SchedulerVisitor hoặc SchedulerListener
    # Dưới đây là ví dụ kiểm tra theo tên rule:
    # -> Ta dựa vào index rule hoặc so sánh chuỗi
    #    parse_tree.toStringTree(recognizer=parser) để in debug.

    # Lấy tên rule con:
    child_rule_name = tree.getChild(0).__class__.__name__  # như "SetEventCmdContext"

    if 'SetEventCmdContext' in child_rule_name:
        # Ta có thể lấy token con để biết time, TEXT,...
        print("Nhận lệnh: Đặt lịch")
        # ...
        # Xử lý đặt lịch: ví dụ gọi hàm tạo event,...
        return "Hệ thống đã ghi nhận lệnh đặt lịch."
    elif 'GetScheduleCmdContext' in child_rule_name:
        print("Nhận lệnh: Xem lịch cho ngày cụ thể")
        # ...
        return "Đây là danh sách sự kiện cho ngày ..."
    elif 'GetDateCmdContext' in child_rule_name:
        print("Nhận lệnh: Hỏi hôm nay là ngày mấy")
        # ...
        return "Hôm nay là ngày 22/03/2025"
    else:
        return "Xin lỗi, tôi chưa hiểu yêu cầu."

def main():
    # Bộ nhận giọng nói
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Xin mời bạn nói (tiếng Việt)...")
        audio = r.listen(source)

    try:
        # Sử dụng Google Speech Recognition 
        text = r.recognize_google(audio, language="vi-VN")
        print("Bạn vừa nói: ", text)

        # Gọi hàm parse
        tree = parse_command(text)

        # Diễn giải ý định và thực thi lệnh
        response = interpret_command(tree)
        print("Bot:", response)

    except Exception as e:
        print("Lỗi nhận giọng hoặc xử lý:", e)

if __name__ == '__main__':
    main()

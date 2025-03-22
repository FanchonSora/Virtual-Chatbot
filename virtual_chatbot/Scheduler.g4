grammar Scheduler;

// Quy tắc gốc
command
   : setEventCmd
   | getScheduleCmd
   | getDateCmd
   ;

// Ví dụ: "đặt lịch lúc 10:30 cho họp nhóm"
setEventCmd
   : 'đặt' 'lịch' 'lúc' time 'cho' TEXT 
   ;

// Ví dụ: "lịch ngày 22/03/2025"
getScheduleCmd
   : 'lịch' 'ngày' date
   ;

// Ví dụ: "hôm nay"
getDateCmd
   : 'hôm' 'nay'
   ;

time
   : TIME
   ;

date
   : DATE
   ;

// Lexer rules
TIME
   : [0-9]{1,2} ':' [0-9]{2}
   ;

DATE
   : [0-9]{1,2} '/' [0-9]{1,2} '/' [0-9]{4}
   ;

// TEXT tạm thời quy định là bất cứ chuỗi nào không chứa dấu xuống dòng, khoảng trắng
TEXT
   : ~[ \t\n\r]+ ( ~[ \t\n\r]* )*
   ;

// Bỏ qua khoảng trắng, xuống dòng
WS
   : [ \t\r\n]+ -> skip
   ;

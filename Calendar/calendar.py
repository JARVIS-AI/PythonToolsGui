import tkinter as tk
import jdatetime
import hijri_converter
from datetime import datetime
import lunardate  # Chinese Lunar Date library

# تعریف رنگ‌ها برای رابط کاربری
BG_COLOR = "#f0f0f0"
FG_COLOR = "#333"

# تابع برای نمایش تاریخ امروز به چهار فرمت مختلف
def show_today_date():
    today_miladi = datetime.now()
    today_shamsi = jdatetime.date.fromgregorian(date=today_miladi)
    today_qamari = hijri_converter.convert.Gregorian(today_miladi.year, today_miladi.month, today_miladi.day).to_hijri()
    
    # محاسبه تاریخ چینی
    today_chinese_lunar = lunardate.LunarDate.fromSolarDate(today_miladi.year, today_miladi.month, today_miladi.day)

    lbl_shamsi.config(text=f"شمسی: {today_shamsi.strftime('%Y/%m/%d')}")
    lbl_miladi.config(text=f"میلادی: {today_miladi.strftime('%Y/%m/%d')}")
    lbl_qamari.config(text=f"قمری: {today_qamari.year}/{today_qamari.month}/{today_qamari.day}")
    lbl_chinese.config(text=f"چینی: {today_chinese_lunar.year}/{today_chinese_lunar.month}/{today_chinese_lunar.day}")

# تابع برای تبدیل تاریخ‌ها
def convert_date():
    try:
        input_date = entry_date.get()
        date_format = date_format_var.get()

        if date_format == "miladi":
            year, month, day = map(int, input_date.split('/'))
            date_miladi = datetime(year, month, day)
            date_shamsi = jdatetime.date.fromgregorian(date=date_miladi)
            date_qamari = hijri_converter.convert.Gregorian(year, month, day).to_hijri()
            date_chinese_lunar = lunardate.LunarDate.fromSolarDate(year, month, day)
        elif date_format == "shamsi":
            year, month, day = map(int, input_date.split('/'))
            date_shamsi = jdatetime.date(year, month, day)
            date_miladi = date_shamsi.togregorian()
            date_qamari = hijri_converter.convert.Gregorian(date_miladi.year, date_miladi.month, date_miladi.day).to_hijri()
            date_chinese_lunar = lunardate.LunarDate.fromSolarDate(date_miladi.year, date_miladi.month, date_miladi.day)
        elif date_format == "qamari":
            year, month, day = map(int, input_date.split('/'))
            date_qamari = hijri_converter.convert.Hijri(year, month, day)
            date_miladi = date_qamari.to_gregorian()
            date_shamsi = jdatetime.date.fromgregorian(date=date_miladi)
            date_chinese_lunar = lunardate.LunarDate.fromSolarDate(date_miladi.year, date_miladi.month, date_miladi.day)

        lbl_convert_shamsi.config(text=f"شمسی: {date_shamsi.strftime('%Y/%m/%d')}")
        lbl_convert_miladi.config(text=f"میلادی: {date_miladi.strftime('%Y/%m/%d')}")
        lbl_convert_qamari.config(text=f"قمری: {date_qamari.year}/{date_qamari.month}/{date_qamari.day}")
        lbl_convert_chinese.config(text=f"چینی: {date_chinese_lunar.year}/{date_chinese_lunar.month}/{date_chinese_lunar.day}")
    except ValueError:
        lbl_convert_shamsi.config(text="خطا: فرمت تاریخ نادرست است")
        lbl_convert_miladi.config(text="")
        lbl_convert_qamari.config(text="")
        lbl_convert_chinese.config(text="")

# ساخت پنجره اصلی برنامه
app = tk.Tk()
app.title("تقویم چندگانه")
app.geometry("450x600")
app.resizable(False, False)
app.configure(bg=BG_COLOR)

# ایجاد ویجت‌ها و قرار دادن آن‌ها در پنجره
lbl_shamsi = tk.Label(app, text="شمسی: ", bg=BG_COLOR, fg=FG_COLOR)
lbl_shamsi.pack()

lbl_miladi = tk.Label(app, text="میلادی: ", bg=BG_COLOR, fg=FG_COLOR)
lbl_miladi.pack()

lbl_qamari = tk.Label(app, text="قمری: ", bg=BG_COLOR, fg=FG_COLOR)
lbl_qamari.pack()

lbl_chinese = tk.Label(app, text="چینی: ", bg=BG_COLOR, fg=FG_COLOR)
lbl_chinese.pack()

btn_show = tk.Button(app, text="نمایش تاریخ امروز", command=show_today_date)
btn_show.pack()

lbl_date_format = tk.Label(app, text="فرمت تاریخ برای تبدیل: YYYY/MM/DD", bg=BG_COLOR, fg=FG_COLOR)
lbl_date_format.pack()

date_format_var = tk.StringVar(app)
date_format_var.set("miladi")  # مقدار پیش‌فرض
date_format_menu = tk.OptionMenu(app, date_format_var, "miladi", "shamsi", "qamari")
date_format_menu.pack()

entry_date = tk.Entry(app)
entry_date.pack()

btn_convert = tk.Button(app, text="تبدیل تاریخ", command=convert_date)
btn_convert.pack()

lbl_convert_shamsi = tk.Label(app, text="تبدیل شده به شمسی: ", bg=BG_COLOR, fg=FG_COLOR)
lbl_convert_shamsi.pack()

lbl_convert_miladi = tk.Label(app, text="تبدیل شده به میلادی: ", bg=BG_COLOR, fg=FG_COLOR)
lbl_convert_miladi.pack()

lbl_convert_qamari = tk.Label(app, text="تبدیل شده به قمری: ", bg=BG_COLOR, fg=FG_COLOR)
lbl_convert_qamari.pack()

lbl_convert_chinese = tk.Label(app, text="تبدیل شده به چینی: ", bg=BG_COLOR, fg=FG_COLOR)
lbl_convert_chinese.pack()

# اضافه کردن لینک آموزشگاه در پایین پنجره
lbl_website = tk.Label(app, text="Made by: JARVIS-AI", bg=BG_COLOR, fg=FG_COLOR)
lbl_website.pack(side=tk.BOTTOM)

# شروع حلقه اصلی برنامه
app.mainloop()

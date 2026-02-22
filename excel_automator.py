import pandas as pd
import numpy as np
from datetime import datetime

def generate_automated_report():
    print("📊 در حال بارگذاری داده‌های خام (شبیه‌سازی سیستم حسابداری)...")
    
    # ساخت داده‌های فروش فرضی برای ۳۰ روز
    np.random.seed(42)
    dates = pd.date_range(start="2024-01-01", periods=30)
    sales = np.random.randint(100, 1000, size=30)
    products = np.random.choice(["لپ‌تاپ", "گوشی موبایل", "هدفون بی‌سیم"], size=30)
    
    # ساخت دیتافریم خام
    raw_df = pd.DataFrame({
        "تاریخ": dates.strftime('%Y-%m-%d'),
        "نام محصول": products,
        "تعداد فروش روزانه": sales
    })
    
    print("⚙️ در حال پردازش و هوشمندسازی گزارش...")
    
    # تحلیل داده‌ها: محاسبه مجموع فروش هر محصول
    summary_df = raw_df.groupby("نام محصول")["تعداد فروش روزانه"].sum().reset_index()
    summary_df.rename(columns={"تعداد فروش روزانه": "کل فروش ماهانه"}, inplace=True)
    
    # محاسبه پرفروش‌ترین محصول
    best_seller = summary_df.loc[summary_df["کل فروش ماهانه"].idxmax()]
    print(f"🏆 پرفروش‌ترین محصول: {best_seller['نام محصول']} (تعداد: {best_seller['کل فروش ماهانه']})")
    
    # ذخیره خروجی در یک فایل اکسل با دو شیت (تب)
    report_filename = f"Smart_Business_Report_{datetime.now().strftime('%Y%m%d')}.xlsx"
    
    try:
        with pd.ExcelWriter(report_filename, engine='openpyxl') as writer:
            raw_df.to_excel(writer, sheet_name='داده‌های خام', index=False)
            summary_df.to_excel(writer, sheet_name='گزارش تحلیلی', index=False)
            
        print(f"\n✅ گزارش اتوماتیک با موفقیت ساخته شد: {report_filename}")
        print("💡 این اسکریپت ساعت‌ها کار دستی را به ۱ ثانیه کاهش می‌دهد!")
    except Exception as e:
        print(f"❌ خطا در ساخت اکسل: {e}")

if __name__ == "__main__":
    generate_automated_report()
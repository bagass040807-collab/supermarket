import streamlit as st
import pandas as pd
import plotly.express as px

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Business Sales Dashboard",
    layout="wide",
    page_icon="📊"
)

# =====================================================
# LANGUAGE (10 LANGUAGES – SEMUA TEKS)
# =====================================================
LANG = {
    "English": {
        "dashboard": "SALES DASHBOARD",
        "upload": "Upload Excel File",
        "mode": "Night Mode",
        "group": "Group Math Business 9",
        "members": "Members",
        "total_sales": "Total Sales",
        "products": "Products Sold",
        "cogs": "Total COGS",
        "rating": "Average Rating",
        "monthly": "Monthly Sales",
        "payment": "Payment Methods",
        "city": "Rating by City",
        "product": "Sales by Product Line",
        "customer": "Sales by Customer Type",
        "preview": "Data Preview",
        "info": "Please upload an Excel file"
    },
    "Indonesia": {
        "dashboard": "DASHBOARD PENJUALAN",
        "upload": "Unggah File Excel",
        "mode": "Mode Malam",
        "group": "Group Math Business 9",
        "members": "Anggota",
        "total_sales": "Total Penjualan",
        "products": "Produk Terjual",
        "cogs": "Total COGS",
        "rating": "Rata-rata Rating",
        "monthly": "Penjualan Bulanan",
        "payment": "Metode Pembayaran",
        "city": "Rating per Kota",
        "product": "Penjualan per Produk",
        "customer": "Penjualan per Tipe Pelanggan",
        "preview": "Pratinjau Data",
        "info": "Silakan unggah file Excel"
    },
    "Chinese": {"dashboard":"销售仪表板","upload":"上传 Excel","mode":"夜间模式","group":"商业数学第9组","members":"成员",
        "total_sales":"总销售额","products":"销售数量","cogs":"总成本","rating":"平均评分","monthly":"每月销售",
        "payment":"支付方式","city":"城市评分","product":"产品销售","customer":"客户类型","preview":"数据预览","info":"请上传 Excel 文件"},
    "Japanese": {"dashboard":"売上ダッシュボード","upload":"Excelをアップロード","mode":"ナイトモード","group":"数学ビジネス第9班","members":"メンバー",
        "total_sales":"総売上","products":"販売数量","cogs":"総コスト","rating":"平均評価","monthly":"月次売上",
        "payment":"支払い方法","city":"都市別評価","product":"商品別売上","customer":"顧客タイプ","preview":"データ表示","info":"Excelをアップロード"},
    "Korean": {"dashboard":"판매 대시보드","upload":"엑셀 업로드","mode":"야간 모드","group":"수학 비즈니스 9조","members":"구성원",
        "total_sales":"총 매출","products":"판매 수량","cogs":"총 비용","rating":"평균 평점","monthly":"월별 매출",
        "payment":"결제 방법","city":"도시별 평점","product":"제품 매출","customer":"고객 유형","preview":"데이터 미리보기","info":"엑셀 업로드"},
    "Spanish": {"dashboard":"TABLERO DE VENTAS","upload":"Subir Excel","mode":"Modo Noche","group":"Grupo Matemática Empresarial 9","members":"Miembros",
        "total_sales":"Ventas Totales","products":"Productos Vendidos","cogs":"Costo Total","rating":"Calificación Promedio","monthly":"Ventas Mensuales",
        "payment":"Métodos de Pago","city":"Calificación por Ciudad","product":"Ventas por Producto","customer":"Tipo de Cliente","preview":"Vista de Datos","info":"Sube archivo Excel"},
    "French": {"dashboard":"TABLEAU DES VENTES","upload":"Télécharger Excel","mode":"Mode Nuit","group":"Groupe Math Business 9","members":"Membres",
        "total_sales":"Ventes Totales","products":"Produits Vendus","cogs":"Coût Total","rating":"Note Moyenne","monthly":"Ventes Mensuelles",
        "payment":"Modes de Paiement","city":"Note par Ville","product":"Ventes par Produit","customer":"Type Client","preview":"Aperçu","info":"Télécharger Excel"},
    "German": {"dashboard":"VERKAUFS-DASHBOARD","upload":"Excel hochladen","mode":"Nachtmodus","group":"Mathe Business Gruppe 9","members":"Mitglieder",
        "total_sales":"Gesamtumsatz","products":"Verkaufte Menge","cogs":"Gesamtkosten","rating":"Durchschnitt","monthly":"Monatlicher Umsatz",
        "payment":"Zahlungsmethoden","city":"Bewertung nach Stadt","product":"Produktumsatz","customer":"Kundentyp","preview":"Vorschau","info":"Excel hochladen"},
    "Arabic": {"dashboard":"لوحة المبيعات","upload":"رفع Excel","mode":"الوضع الليلي","group":"مجموعة رياضيات الأعمال 9","members":"الأعضاء",
        "total_sales":"إجمالي المبيعات","products":"الكمية","cogs":"إجمالي التكلفة","rating":"متوسط التقييم","monthly":"المبيعات الشهرية",
        "payment":"طرق الدفع","city":"التقييم حسب المدينة","product":"مبيعات المنتج","customer":"نوع العميل","preview":"عرض البيانات","info":"يرجى رفع الملف"},
    "Thai": {"dashboard":"แดชบอร์ดยอดขาย","upload":"อัปโหลด Excel","mode":"โหมดกลางคืน","group":"กลุ่มคณิตธุรกิจ 9","members":"สมาชิก",
        "total_sales":"ยอดขายรวม","products":"จำนวนขาย","cogs":"ต้นทุนรวม","rating":"คะแนนเฉลี่ย","monthly":"ยอดขายรายเดือน",
        "payment":"การชำระเงิน","city":"คะแนนตามเมือง","product":"ยอดขายสินค้า","customer":"ประเภทลูกค้า","preview":"แสดงข้อมูล","info":"อัปโหลดไฟล์"}
}

# =====================================================
# SIDEBAR
# =====================================================
lang = st.sidebar.selectbox("🌐 Language", LANG.keys())
T = LANG[lang]

night = st.sidebar.toggle(f"🌙 {T['mode']}")

file = st.sidebar.file_uploader(T["upload"], type=["xlsx"])

# ===== GROUP CARD =====
st.sidebar.markdown(f"""
<div style="padding:14px;border-radius:12px;
background:{'#0f2a44' if not night else '#111'};
color:white;font-weight:800;text-align:center;">
{T['group']}
</div>
""", unsafe_allow_html=True)

st.sidebar.markdown(f"### {T['members']}")

for m in ["Bagas Christian","Chesya Anggelita","Gwyneth Anggun","Rebecca Dearly"]:
    st.sidebar.markdown(f"""
    <div style="padding:10px;margin-bottom:10px;border-radius:10px;
    background:{'#ffffff' if not night else '#1c1c1c'};
    color:{'#000' if not night else '#fff'};
    font-weight:600;">
    {m}
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# MAIN
# =====================================================
bg = "#f4f6fa" if not night else "#0e1117"
text = "#000" if not night else "#fff"
chart_colors = ["#1f4f82","#3a6ea5","#6f9fd8","#b5cdef"]

st.markdown(f"<style>body{{background:{bg};color:{text};}}</style>", unsafe_allow_html=True)

if file:
    df = pd.read_excel(file)
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    df["Month"] = df["Date"].dt.to_period("M").dt.to_timestamp()

    st.markdown(f"<h1 style='text-align:center;color:{text}'>{T['dashboard']}</h1>", unsafe_allow_html=True)

    # KPI
    k1,k2,k3,k4 = st.columns(4)
    k1.metric(T["total_sales"], f"${df['Total'].sum():,.2f}")
    k2.metric(T["products"], int(df["Quantity"].sum()))
    k3.metric(T["cogs"], f"${df['cogs'].sum():,.2f}")
    k4.metric(T["rating"], f"{df['Rating'].mean():.2f}")

    # ===== CHART STYLE =====
    def style(fig, title):
        fig.update_layout(
            title=dict(text=title, x=0.5, font=dict(color=text)),
            paper_bgcolor=bg,
            plot_bgcolor=bg,
            font=dict(color=text)
        )
        return fig

    st.plotly_chart(style(
        px.line(df.groupby("Month")["Total"].sum().reset_index(),
                x="Month", y="Total",
                markers=True,
                color_discrete_sequence=chart_colors),
        T["monthly"]), True)

    c1,c2 = st.columns(2)
    c1.plotly_chart(style(px.pie(df, names="Payment", color_discrete_sequence=chart_colors), T["payment"]), True)
    c2.plotly_chart(style(px.bar(df.groupby("City")["Rating"].mean().reset_index(),
                                 x="City", y="Rating",
                                 color_discrete_sequence=chart_colors), T["city"]), True)

    c3,c4 = st.columns(2)
    c3.plotly_chart(style(px.bar(df.groupby("Product line")["Total"].sum().reset_index(),
                                 x="Product line", y="Total",
                                 color_discrete_sequence=chart_colors), T["product"]), True)
    c4.plotly_chart(style(px.bar(df.groupby("Customer type")["Total"].sum().reset_index(),
                                 x="Customer type", y="Total",
                                 color_discrete_sequence=chart_colors), T["customer"]), True)

    st.markdown(f"### {T['preview']}")
    st.dataframe(df, use_container_width=True)

else:
    st.info(T["info"])

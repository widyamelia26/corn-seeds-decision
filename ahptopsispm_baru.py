import streamlit as st
import numpy as np
import pandas as pd
import base64
from numpy.linalg import norm
import matplotlib.pyplot as plt

# ---------- SET BACKGROUND GAMBAR ----------
def set_background(image_file):
    with open(image_file, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()

    css = f"""
    <style>
    /* 🌄 Background utama */
    .stApp {{
        background-image: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.85)), url("data:image/png;base64,{encoded}"); 
        background-size: cover;
        background-attachment: fixed;
    }}

    /* 🌿 Sidebar */
    section[data-testid="stSidebar"] {{
        background-color: #11312de3;
        color: black;
    }}
    div[data-testid="stVerticalBlock"] > div {{
        background-color: rgba(224, 225, 226, 0.6);
        padding: 10px;
        border-radius: 10px;
    }}
    .stApp, .stApp * {{
        color: black !important;
    }}

    /* Input umum */
    input, select, textarea {{
        background-color: rgba(224, 225, 226, 0.6) !important;
        color: #000 !important;
        border-radius: 4px !important;
    }}

    /* 🔥 FULL SELECTBOX (khusus sidebar selectbox) */
    section[data-testid="stSidebar"] div[role="combobox"],
    section[data-testid="stSidebar"] div[role="combobox"] > div,
    section[data-testid="stSidebar"] div[role="combobox"] > div > div,
    section[data-testid="stSidebar"] div[role="combobox"] * {{
        background-color: rgba(224, 225, 226, 0.8) !important;
        color: black !important;
        border: 1px solid #ccc !important;
        border-radius: 8px !important;
    }}

    /* ✅ Jika ada outer wrapper (contoh class yang kamu kasih: st-c4), kita sikat semua */
    section[data-testid="stSidebar"] div[class*="st-c"],
    section[data-testid="stSidebar"] div[class*="st-c"] * {{
        background-color: rgba(224, 225, 226, 0.8) !important;
        color: black !important;
    }}

    /* Listbox dropdown */
    ul[role="listbox"],
    ul[role="listbox"] li {{
        background-color: rgba(224, 225, 226, 0.95) !important;
        color: black !important;
    }}

    /* Tombol */
    button[kind="secondary"], button[kind="primary"] {{
        background-color: rgba(224, 225, 226, 0.8) !important;
        color: #000 !important;
        border: 1px solid #ccc !important;
        border-radius: 8px !important;
    }}
    button[kind="secondary"]:hover, button[kind="primary"]:hover {{
        background-color: #e0e0e0 !important;
    }}
    ::placeholder {{
        color: #555 !important;
    }}
    /* 🔢 Tombol +/- di number_input (konten utama) */
    div[data-baseweb="input"] button {{
        background-color: rgba(224, 225, 226, 0.8) !important;
        color: black !important;
        border: 1px solid #ccc !important;
        border-radius: 0 8px 8px 0 !important;
    }}
    /* 🔢 Tombol + dan - di number_input */
    button[data-testid="stNumberInputStepUp"],
    button[data-testid="stNumberInputStepDown"] {{
        background-color: rgba(250, 250, 250, 0.6) !important;
        color: black !important;
        border: 1px solid #ccc !important;
        margin: 0 !important;
        padding: 0.5rem !important;
        border-left: none !important;  /* Biar nyatu dengan input */
        height: 100% !important;
        box-sizing: border-box;
    }}

    /* Kasih radius di kanan (biar smooth) */
    button[data-testid="stNumberInputStepUp"] {{
        border-top-right-radius: 8px !important;
        border-bottom-right-radius: 8px !important;
    }}
    button[data-testid="stNumberInputStepDown"] {{
        border-top-left-radius: 0 !important;
        border-bottom-left-radius: 0 !important;
    }}

    /* Hover effect */
    button[data-testid="stNumberInputStepUp"]:hover,
    button[data-testid="stNumberInputStepDown"]:hover {{
        background-color: #e0e0e0 !important;
    }}

    /* Opsional: SVG icon lebih besar dan tengah */
    button[data-testid="stNumberInputStepUp"] svg,
    button[data-testid="stNumberInputStepDown"] svg {{
        fill: black !important;
        width: 8px !important;
        height: 8px !important;
    }}
    /* 🌿 Header hijau tua dengan teks terang */
    header[data-testid="stHeader"] {{
        background-color: #223a38!important; /* hijau tua */
        color: #ffffff !important;            /* teks putih */
        border-bottom: none !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
    }}

    /* Pastikan semua teks/ikon di header juga terang */
    header[data-testid="stHeader"] * {{
        color: #ffffff !important;
        fill: #88a5a3 !important;  /* untuk SVG/icon */
    }}

    /* 🌿 Semua SLIDER rail pakai linear-gradient */
    div[data-baseweb="slider"] > div > div:nth-child(1) {{
        background: linear-gradient(
            to right,
            #295325 0%,
            #293d27 100%
        ) !important;
        height: 3px !important;
        border-radius: 999px !important;
        opacity: 1 !important;
    }}

    /* 🚫 Matikan track aktif (yang bikin merah) */
    div[data-baseweb="slider"] > div > div:nth-child(2) {{
        background: none !important;
        background-image: none !important;
        box-shadow: none !important;
        opacity: 2 !important;
        visibility: visible !important;
        height: 3px !important;
    }}

    /* 🌿 Handle (knob) */
    div[data-baseweb="slider"] div[role="slider"] {{
        background-color: #295325 !important;
        border: 2px solid #fff !important;
    }}
    /* 🌿 st.selectbox di konten utama */
    div[data-testid="stSelectbox"] {{
        background-color: #f5f5f500 !important;  /* putih soft */
        border: 0px solid #ccc !important;
        border-radius: 8px !important;
        color: black !important;
    }}

    /* 🌿 Inner content selectbox */
    div[data-testid="stSelectbox"] * {{
        background-color: #f5f5f500!important;
        color: black !important;
        font-size: 14px !important;
    }}

    /* 🌿 Dropdown listbox */
    ul[role="listbox"],
    ul[role="listbox"] li {{
        background-color: #f5f5f5 !important;
        color: black !important;
    }}

    /* Hover effect (opsional) */
    ul[role="listbox"] li:hover {{
        background-color: #f5f5f500 !important;
    }}
    /* 🔧 Override webkit text fill color */
    .stApp * {{
        -webkit-text-fill-color: black !important;
    }}
    
    /* 🎯 Khusus ikon collapse sidebar */
    div[data-testid="stSidebarCollapseButton"] svg path:first-of-type {{
        fill: none !important;
    }}
    div[data-testid="stSidebarCollapseButton"] svg path:last-of-type {{
        fill: white !important;
    }}

    /* 🎯 Untuk ikon collapsed sidebar */
    div[data-testid="stSidebarCollapsedButton"] svg path:first-of-type {{
        fill: none !important;
    }}
    div[data-testid="stSidebarCollapsedButton"] svg path:last-of-type {{
        fill: white !important;
    }}

    /* 🎨 Kotak putih di tombol “Deploy” */
    button[data-testid="stBaseButton-header"] {{
        background-color: #88a5a3 !important;
        color: #000000 !important;
        border: none !important;
        padding: 0.5rem 1rem !important;
        border-radius: 0.5rem !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
    }}

    /* Hover effect (opsional) */
    button[data-testid="stBaseButton-header"]:hover {{
        background-color: #f0f0f0 !important;
    }}

    /* 🎯 Buat titik tiga (MainMenu) jadi hitam */
    span[data-testid="stMainMenu"] svg path:last-of-type {{
        fill: black !important;
    }}

    </style>
    """
    
    st.markdown(css, unsafe_allow_html=True)

# ---------- FUNGSI AHP ----------
@st.cache_data
def get_weight(A, str):
    n = A.shape[0]
    
    # Normalisasi matriks untuk mendapatkan prioritas
    normalized = A / A.sum(axis=0)
    priorities = normalized.mean(axis=1)  # Prioritas adalah rata-rata normalisasi
    
    # Menghitung weighted sum dan lambda_max
    weighted_sum = np.dot(A, priorities)
    lambda_max = (weighted_sum / priorities).mean()

    # Consistency Index (CI) dan Consistency Ratio (CR)
    ci = (lambda_max - n) / (n - 1)
    ri_dict = {1: 0.00, 2: 0.00, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24,
               7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49, 11: 1.51}
    ri = ri_dict.get(n, 1.49)
    cr = ci / ri if ri else 0
    
    # Menampilkan hasil perhitungan CI dan CR
    print("The normalized eigen vector:")
    print(priorities)
    print(f"Lambda_max: {lambda_max}")
    print(f"CR = {cr}")
    
    if cr >= 0.1:
        print(f"Failed Consistency check of {str}")
        st.error(f"Konsistensi {str} belum terpenuhi, sehingga hasil analisis berisiko bias. Mohon tinjau dan perbaiki penilaian pada pasangan kriteria yang berpotensi bermasalah agar konsistensi tercapai dan hasil analisis lebih akurat. ")
    
    return priorities

# ---------- FUNGSI TOPSIS ----------
def normalize_matrix(D):
    D = np.array(D, dtype=float)
    norm = np.linalg.norm(D, axis=0)
    return D / norm

def weighted_normalized_matrix(Dnorm, W):
    W = np.array(W)
    return Dnorm * W

def ideal_solutions(Y, is_benefit):
    A_plus = []
    A_minus = []
    for j in range(Y.shape[1]):
        if is_benefit[j]:
            A_plus.append(np.max(Y[:, j]))
            A_minus.append(np.min(Y[:, j]))
        else:
            A_plus.append(np.min(Y[:, j]))
            A_minus.append(np.max(Y[:, j]))
    return np.array(A_plus), np.array(A_minus)

def separation_measures(Y, A_plus, A_minus):
    D_plus = np.linalg.norm(Y - A_plus, axis=1)
    D_minus = np.linalg.norm(Y - A_minus, axis=1)
    return D_plus, D_minus

def relative_closeness(D_plus, D_minus):
    return D_minus / (D_plus + D_minus)

def topsis(D, W, is_benefit):
    Dnorm = normalize_matrix(D)
    Y = weighted_normalized_matrix(Dnorm, W)
    A_plus, A_minus = ideal_solutions(Y, is_benefit)
    D_plus, D_minus = separation_measures(Y, A_plus, A_minus)
    S = relative_closeness(D_plus, D_minus)
    ranking = np.argsort(S)[::-1]
    return S, ranking

# ---------- PROFILE MATCHING ----------
def gap_weight(gap):
    mapping = {
        0: 5, 1: 4.5, -1: 4.5,
        2: 4, -2: 4,
        3: 3.5, -3: 3.5,
        4: 3, -4: 3,
        5: 2.5, -5: 2.5
    }
    return mapping.get(gap, 1)

def range_w(val, mn, mx, ideal):
    # interpolasi tri-segitiga untuk range criterion
    if ideal >= mn and ideal <= mx:
        return 5.0
    if val <= ideal:
        return (val - mn)/(ideal - mn)*4 + 1
    return (mx - val)/(mx - ideal)*-4+5

def profile_matching(criteria, alternatives, scores):
    cf_weights = [c['weight'] for c in criteria if c['kind'] == 'CF (Core Factor)']
    sf_weights = [c['weight'] for c in criteria if c['kind'] == 'SF (Secondary Factor)']
    total_cf_weight = sum(cf_weights)
    total_sf_weight = sum(sf_weights)

    # Check if CF weight is below 50%
    if total_cf_weight < 0.5:
        st.warning(f"Bobot Core Factor (CF) kurang dari 50% ({total_cf_weight:.2%}).")

        # Rekomendasi: ambil SF dengan bobot terbesar
        sf_candidates = sorted(
        [c for c in criteria if c['kind'].startswith("SF")],
        key=lambda x: x['weight'],
        reverse=True)

        # Cari kombinasi minimal SF untuk dijadikan CF agar total CF ≥ 0.5
        accumulated = total_cf_weight
        added = []
        for c in sf_candidates:
            accumulated += c['weight']
            added.append(c['name'])
            if accumulated >= 0.5:
                break

        # Tampilkan rekomendasi
        if added:
            if len(added) == 1:
                st.info(
                    f"Untuk memenuhi ketentuan bobot CF ≥ 50%, "
                    f"pertimbangkan **'{added[0]}'** sebagai Core Factor. "
                    "Silakan ulangi konfigurasi dan ubah jenis kriteria tersebut menjadi CF."
                )
            else:
                kriteria_str = ", ".join(f"'{k}'" for k in added)
                st.info(
                    f"Untuk memenuhi ketentuan bobot CF ≥ 50%, pertimbangkan kriteria berikut "
                    f"sebagai Core Factor: {kriteria_str}. "
                    "Silakan ulangi konfigurasi dan ubah jenis kriteria tersebut menjadi CF."
                )

    # # Check if CF weight is below 50%
    # if total_cf_weight < 0.5:
    #     # Identify criteria that are SF but should be CF
    #     added = [c['name'] for c in criteria if c['kind'] == 'SF (Secondary Factor)' and c['weight'] > 0]
        
    #     if added:
    #         if len(added) == 1:
    #             st.info(f"Untuk memenuhi ketentuan bobot CF ≥ 50%, pertimbangkan **'{added[0]}'** sebagai Core Factor. Silakan ulangi konfigurasi dan ubah jenis kriteria tersebut menjadi CF.")
    #         else:
    #             kriteria_str = ", ".join(f"'{k}'" for k in added)
    #             st.info(f"Untuk memenuhi ketentuan bobot CF ≥ 50%, pertimbangkan kriteria berikut sebagai Core Factor: {kriteria_str}. Silakan ulangi konfigurasi dan ubah jenis kriteria tersebut menjadi CF.")

    # Calculate gap weights for CF and SF
    gap_weights = pd.DataFrame(index=alternatives, columns=[c['name'] for c in criteria])
    for c in criteria:
        name, ideal = c['name'], c['ideal']
        for alt in alternatives:
            val = scores[alt][name]
            if isinstance(val, (list, tuple)):
                mn, mx = val
                mid = (mn + mx) / 2
                gw = range_w(mid, mn, mx, ideal)
            else:
                gap_int = int(np.round(val - ideal))
                gw = gap_weight(gap_int)
            gap_weights.loc[alt, name] = gw

    # Calculate CF and SF scores
    cf_score = gap_weights[[c['name'] for c in criteria if c['kind'] == 'CF (Core Factor)']].astype(float).mean(axis=1) if cf_weights else pd.Series(0, index=alternatives)
    sf_score = gap_weights[[c['name'] for c in criteria if c['kind'] == 'SF (Secondary Factor)']].astype(float).mean(axis=1) if sf_weights else pd.Series(0, index=alternatives)

    total_score = cf_score * total_cf_weight + sf_score * total_sf_weight

    # Create result DataFrame and sort based on total score
    result = pd.DataFrame({
        "Varietas": alternatives,
        "CF Score": cf_score,
        "SF Score": sf_score,
        "Total Score": total_score
    }).sort_values(by="Total Score", ascending=False)

    # Add Ranking
    result["Ranking"] = range(1, len(result) + 1)

    # # === Build result including gap_weights per criterion ===
    # # copy gap_weights (index=alternatives, cols=criteria names)
    # result = gap_weights.astype(float).copy()
    # # append the CF/SF/Total scores
    # result["CF Score"]    = cf_score
    # result["SF Score"]    = sf_score
    # result["Total Score"] = total_score
    # # sort descending by total score
    # result = result.sort_values(by="Total Score", ascending=False)
    # # add ranking column
    # result["Ranking"] = range(1, len(result) + 1)
    # # move index (alternative names) into a proper column
    # result = result.reset_index().rename(columns={"index":"Varietas"})

    return result

# ---------- APLIKASI STREAMLIT ----------

def main():
    st.set_page_config(page_title="DSS Bibit Jagung", layout="wide")
    set_background("jagung(1).jpeg")

    st.markdown("""
    <style>
    .block-container { padding-top: 0 !important; }
    .custom-header { margin: 1rem rem 0.5rem 0 !important; }
    </style>
    <h1 class="custom-header">🌽 Sistem Pendukung Keputusan Pemilihan Bibit Jagung</h1>
    """, unsafe_allow_html=True)

    # ---------- INPUT JUMLAH ---------- 
    st.sidebar.subheader("\U0001F522 Jumlah Varietas dan Kriteria")
    num_alternatives = st.sidebar.number_input("Jumlah Varietas", min_value=2, max_value=20, value=4, step=1)
    num_criteria = st.sidebar.number_input("Jumlah Kriteria", min_value=2, max_value=20, value=4, step=1)

    # ---------- INPUT NAMA ALTERNATIF & KRITERIA ----------
    st.sidebar.subheader("\U0001F4DD Nama Varietas dan Kriteria")
    st.sidebar.markdown("**Nama Varietas:**")
    alternatives = []
    for i in range(num_alternatives):
        alternatives.append(st.sidebar.text_input(f"Varietas {i+1}", value=f"Varietas {i+1}", key=f"alt_{i}"))
    
    st.sidebar.markdown("**Nama Kriteria:**")
    criteria = []
    for i in range(num_criteria):
        criteria_name = st.sidebar.text_input(f"Kriteria {i+1}", value=f"Kriteria {i+1}", key=f"cri_{i}")
        # Initialize criteria as a dictionary for each entry
        criteria.append({
            'name': criteria_name,
            'kind': '',  # Empty initially, will be filled later
            'ideal': 5   # Default ideal value, can be updated
        })

    # ---------- PILIH METODE ---------- 
    st.sidebar.subheader("Pilih Metode Pengambilan Keputusan")  
    method = st.sidebar.selectbox("", ["AHP", "TOPSIS", "Profile Matching"], index=None, placeholder="Pilih Metode")
    
    if method == "AHP":
        # ---------- INPUT PERBANDINGAN BERPASANGAN UNTUK KRITERIA ----------
        st.subheader("Perbandingan Berpasangan untuk Kriteria")
        A = np.ones((num_criteria, num_criteria))
        
        # Membungkus perbandingan dalam expanders
        for i in range(num_criteria):
            for j in range(i + 1, num_criteria):
                if i != j:
                    with st.expander(f"🔍✨ Bandingkan {criteria[i]['name']} dengan {criteria[j]['name']}", expanded=True):
                        # Menyusun pilihan radio dan slider dalam kolom yang lebih rapi
                        col1, col2 = st.columns([1, 3])

                        with col1:
                            # Pilihan perbandingan secara horizontal
                            higher_priority = st.radio(
                                f"Pilih kriteria yang lebih tinggi antara {criteria[i]['name']} dan {criteria[j]['name']}",
                                options=[criteria[i]['name'], criteria[j]['name']],
                                key=f"priority_criteria_{i}_{j}",
                                horizontal=True
                            )

                        with col2:
                            # Teks perbandingan yang dinamis
                            if higher_priority == criteria[i]['name']:
                                comparison_text = f"Seberapa besar {criteria[i]['name']} lebih penting dibandingkan {criteria[j]['name']}"
                            else:
                                comparison_text = f"Seberapa besar {criteria[j]['name']} lebih penting dibandingkan {criteria[i]['name']}"

                            # Slider untuk AHP dengan label deskriptif
                            value = st.slider(
                                comparison_text, 
                                min_value=1, max_value=9, step=1,
                                value=1,
                                key=f"slider_criteria_{i}_{j}",
                                format="%.0f",
                            )

                            # Mengubah angka slider menjadi label deskriptif
                            label_dict = {
                                1: "sama penting",
                                2: "mendekati sedikit lebih penting",
                                3: "sedikit lebih penting",
                                4: "mendekati lebih penting",
                                5: "lebih penting dari",
                                6: "mendekati sangat penting",
                                7: "sangat penting",
                                8: "mendekati mutlak",
                                9: "mutlak sangat penting"
                            }
                            
                            selected_label = label_dict.get(value, "Unknown")
                            
                            # Menampilkan label deskriptif di bawah slider
                            st.write(f"Skor: {selected_label}")

                            # Update nilai matriks perbandingan berpasangan
                            if higher_priority == criteria[i]['name']:
                                A[i][j] = value
                                A[j][i] = 1 / value
                            else:
                                A[j][i] = value
                                A[i][j] = 1 / value
        # st.write("pairwise kriteria", A)

        # ---------- INPUT PERBANDINGAN BERPASANGAN UNTUK ALTERNATIF ----------
        st.subheader("Perbandingan Berpasangan untuk Setiap Varietas Jagung")
        B = np.ones((num_criteria, num_alternatives, num_alternatives))
        for k in range(num_criteria):
            with st.expander(f"🔍✨ Bandingkan Setiap Varietas untuk Kriteria {criteria[k]['name']}"):
                for i in range(num_alternatives):
                    for j in range(i + 1, num_alternatives):
                        if i != j:
                            # Membagi perbandingan alternatif menggunakan kolom
                            col1, col2 = st.columns([1, 3])

                            with col1:
                                # Pilihan perbandingan secara horizontal
                                higher_priority = st.radio(
                                    f"Pilih Varietas yang lebih baik antara {alternatives[i]} dan {alternatives[j]}",
                                    options=[alternatives[i], alternatives[j]],
                                    key=f"priority_alternative_{k}_{i}_{j}",
                                    horizontal=True
                                )

                            with col2:
                                # Teks perbandingan yang dinamis
                                if higher_priority == alternatives[i]:
                                    comparison_text = f"Seberapa besar {alternatives[i]} lebih baik dibandingkan {alternatives[j]}"
                                else:
                                    comparison_text = f"Seberapa besar {alternatives[j]} lebih baik dibandingkan {alternatives[i]}"

                                # Slider untuk AHP dengan label deskriptif
                                value = st.slider(
                                    comparison_text, 
                                    min_value=1, max_value=9, step=1,
                                    value=1,
                                    key=f"slider_alternative_{k}_{i}_{j}",
                                    format="%.0f",
                                )

                                # Mengubah angka slider menjadi label deskriptif
                                label_dict = {
                                    1: "sama penting",
                                    2: "mendekati sedikit lebih penting",
                                    3: "sedikit lebih penting",
                                    4: "mendekati lebih penting",
                                    5: "lebih penting dari",
                                    6: "mendekati sangat penting",
                                    7: "sangat penting",
                                    8: "mendekati mutlak",
                                    9: "mutlak sangat penting"
                                }
                                
                                selected_label = label_dict.get(value, "Unknown")
                                
                                # Menampilkan label deskriptif di bawah slider
                                st.write(f"Skor: {selected_label}")
                            
                                # Update nilai matriks perbandingan berpasangan
                                if higher_priority == alternatives[i]:
                                    B[k][i][j] = value
                                    B[k][j][i] = 1 / value
                                else:
                                    B[k][j][i] = value
                                    B[k][i][j] = 1 / value
            # st.write(f"### Matriks Perbandingan untuk Kriteria: {criteria[k]['name']}")
            # df_B = pd.DataFrame(B[k], index=alternatives, columns=alternatives)
            # st.dataframe(df_B)

        # ---------- TOMBOL UNTUK MENENTUKAN ALTERNATIF DENGAN AHP ----------
        if st.button("\U0001F50E Tentukan Varietas dengan AHP"):
            W2 = get_weight(A, "Kriteria")

            # Perhitungan bobot alternatif untuk setiap kriteria
            W3 = np.zeros((num_criteria, num_alternatives))
            for k in range(num_criteria):
                W3[k] = get_weight(B[k], f"skor varietas untuk kriteria {criteria[k]['name']}")

            # Menghitung skor total untuk setiap alternatif
            W = np.dot(W2, W3)  # Skor AHP untuk alternatif

            # ---------- Menampilkan Hasil Skor dan Ranking AHP ----------
            st.subheader("Hasil Ranking Varietas Berdasarkan AHP")
            
            # Sort the results by Skor AHP and then assign ranks accordingly
            sorted_indices = np.argsort(W)[::-1]  # Sort indices by descending order of W
            sorted_scores = [round(W[i], 4) for i in sorted_indices]
            sorted_alternatives = [alternatives[i] for i in sorted_indices]
            
            result_df = pd.DataFrame({
                "Alternatif": sorted_alternatives,
                "Skor AHP": sorted_scores,
                "Ranking": list(range(1, len(alternatives) + 1))  # Assign ranks from 1 to n
            }).reset_index(drop=True)

            st.dataframe(result_df, use_container_width=True, hide_index=True)

            best_choice = result_df.iloc[0]
            st.success(f"Varietas terbaik berdasarkan AHP adalah **{best_choice['Alternatif']}** dengan skor {best_choice['Skor AHP']:.4f}.")

            st.markdown(f"""
            ### \U0001F4DD Kesimpulan
            Berdasarkan hasil perhitungan dengan metode AHP, bibit jagung **{best_choice['Alternatif']}** merupakan pilihan terbaik
            karena memiliki skor paling tinggi. Bibit ini diharapkan memberikan hasil paling optimal berdasarkan kriteria yang telah ditentukan.
            """)

    elif method == "TOPSIS":
        # ---------- PILIH METODE PEMBOBOTAN ----------
        st.subheader("\u2699\ufe0f Metode Pembobotan")
        weighting_method = st.radio("Pilih metode pembobotan kriteria:", ["Manual", "AHP"], horizontal=True)

        # ---------- PEMBOBOTAN MANUAL ----------
        if weighting_method == "Manual":
            # ---------- INPUT BOBOT DAN TIPE KRITERIA ---------- 
            st.subheader("\u2699\ufe0f Bobot dan Tipe Kriteria")

            # Membuat dua kolom untuk Bobot dan Tipe Kriteria
            col1, col2 = st.columns(2)

            weights = []
            is_benefit_list = []

            # Kolom pertama untuk Bobot
            with col1:
                for i in range(num_criteria - 1):  # Kurangi 1 karena kriteria terakhir akan dihitung otomatis
                    weight = st.number_input(f"Bobot untuk {criteria[i]['name']}", min_value=0.0000, max_value=1.0000, value=0.0001, step=0.0001, format='%.4f', key=f"weight_{i}")
                    weights.append(weight)

                # Hitung bobot kriteria terakhir sebagai sisa dari total 1
                remaining_weight = round(1.0 - sum(weights), 4)
                if remaining_weight < 0:
                    st.warning("⚠️ Total bobot melebihi 1. Bobot terakhir akan diset 0.")
                    remaining_weight = 0.0
                weights.append(remaining_weight)
                st.number_input(f"Bobot ({criteria[-1]['name']})", value=remaining_weight, format="%.4f", disabled=True, key=f"w_topsis_auto_{-1}")
            # Kolom kedua untuk Tipe Kriteria
            with col2:
                for i in range(num_criteria):
                    is_benefit = st.selectbox(f"Tipe untuk {criteria[i]['name']}", ["Benefit", "Cost"], key=f"benefit_{i}")
                    is_benefit_list.append(is_benefit == "Benefit")

        # ---------- PEMBOBOTAN AHP ----------
        elif weighting_method == "AHP":
            # Matriks perbandingan berpasangan untuk kriteria
            st.subheader("Matriks Perbandingan Berpasangan Kriteria (AHP)")
            A = np.ones((num_criteria, num_criteria))

            for i in range(num_criteria):
                for j in range(i + 1, num_criteria):
                    if i != j:
                        # Menggunakan expander untuk setiap perbandingan
                        with st.expander(f"🔍✨Bandingkan {criteria[i]['name']} dengan {criteria[j]['name']}"):
                            # Membuat kolom untuk memisahkan pilihan dan slider
                            col1, col2 = st.columns([1, 3])

                            with col1:
                                # Pilihan perbandingan secara horizontal
                                higher_priority = st.radio(
                                    f"Pilih kriteria yang lebih tinggi antara {criteria[i]['name']} dan {criteria[j]['name']}",
                                    options=[criteria[i]['name'], criteria[j]['name']],
                                    key=f"priority_criteria_{i}_{j}",
                                    horizontal=True  # Pilihan radio ditampilkan secara horizontal
                                )

                            with col2:
                                # Teks perbandingan yang dinamis
                                if higher_priority == criteria[i]['name']:
                                    comparison_text = f"Seberapa besar {criteria[i]['name']} lebih penting dibandingkan {criteria[j]['name']}"
                                else:
                                    comparison_text = f"Seberapa besar {criteria[j]['name']} lebih penting dibandingkan {criteria[i]['name']}"

                                # Slider untuk AHP dengan label deskriptif
                                value = st.slider(
                                    comparison_text, 
                                    min_value=1, max_value=9, step=1,
                                    value=1,
                                    key=f"slider_criteria_{i}_{j}",
                                    format="%.0f",
                                )

                                # Mengubah angka slider menjadi label deskriptif
                                label_dict = {
                                    1: "sama penting",
                                    2: "mendekati sedikit lebih penting",
                                    3: "sedikit lebih penting",
                                    4: "mendekati lebih penting",
                                    5: "lebih penting dari",
                                    6: "mendekati sangat penting",
                                    7: "sangat penting",
                                    8: "mendekati mutlak",
                                    9: "mutlak sangat penting"
                                }
                                
                                selected_label = label_dict.get(value, "Unknown")
                                
                                # Menampilkan label deskriptif di bawah slider
                                st.write(f"Skor: {selected_label}")

                                # Update nilai matriks perbandingan berpasangan
                                if higher_priority == criteria[i]['name']:
                                    A[i][j] = value
                                    A[j][i] = 1 / value
                                else:
                                    A[j][i] = value
                                    A[i][j] = 1 / value

            # Perhitungan bobot kriteria berdasarkan AHP
            weights = get_weight(A, "Kriteria")

            # ---------- Tipe Kriteria ----------
            st.subheader("\U0001F4D6 Tipe Kriteria")
            is_benefit_list = []
            for i in range(num_criteria):
                is_benefit = st.selectbox(f"Tipe untuk {criteria[i]['name']}", ["Benefit", "Cost"], key=f"benefit_{i}")
                is_benefit_list.append(is_benefit == "Benefit")

        # ---------- INPUT MATRKS KEPUTUSAN ----------
        st.subheader("\U0001F4CB Input Matriks Keputusan")
        # Convert `criteria` to a list of just the names (strings) for the columns
        criteria_names = [criterion['name'] for criterion in criteria]

        # Create the DataFrame with the correct column names (strings only)
        matrix_df = pd.DataFrame(
            np.zeros((num_alternatives, num_criteria)),
            columns=criteria_names,
            index=alternatives
        )

        # Use the data editor to allow input
        matrix_df = st.data_editor(matrix_df, key="matrix_editor", num_rows="fixed", use_container_width=True)


        # ---------- HITUNG TOPSIS ----------
        if st.button("\U0001F50E Tentukan Varietas Jagung dengan TOPSIS"):
            try:
                matrix = matrix_df.values.tolist()  # Matriks keputusan yang sudah diinput
                # Skor TOPSIS dihitung menggunakan matriks keputusan, bobot, dan tipe kriteria
                scores, ranking = topsis(matrix, weights, is_benefit_list)

                # Menampilkan hasil TOPSIS
                st.success("\u2705 Perhitungan selesai!")
                st.markdown("---")
                st.subheader("\U0001F4CA Hasil Ranking Varietas Bibit Jagung")

                result_df = pd.DataFrame({
                    "Alternatif": alternatives,
                    "Skor TOPSIS": [round(s, 4) for s in scores],
                    "Ranking": [int(np.where(ranking == i)[0][0]) + 1 for i in range(len(alternatives))]
                }).sort_values(by="Skor TOPSIS", ascending=False).reset_index(drop=True)

                st.dataframe(result_df, use_container_width=True, hide_index=True)

                best_choice = result_df.iloc[0]
                st.success(f"Varietas terbaik adalah **{best_choice['Alternatif']}** dengan skor {best_choice['Skor TOPSIS']:.4f}.")
                st.markdown(f"""
                ### \U0001F4DD Kesimpulan
                Berdasarkan hasil perhitungan dengan metode TOPSIS, bibit jagung **{best_choice['Alternatif']}** merupakan pilihan terbaik
                karena memiliki skor kedekatan relatif tertinggi terhadap solusi ideal. Bibit ini diharapkan memberikan 
                hasil paling optimal berdasarkan kriteria yang telah ditentukan.""")
            except Exception as e:
                st.error(f"Terjadi kesalahan dalam perhitungan: {e}")

    elif method == "Profile Matching":
        # ---------- PROFILE MATCHING INPUT ----------
        st.subheader("Input Jenis Kriteria dan Nilai Ideal untuk Profile Matching")

        # Loop untuk setiap kriteria
        for i in range(num_criteria):
            # Buat 3 kolom
            col1, col2, col3 = st.columns(3)

            with col1:
                # Jenis Kriteria (Core Factor or Secondary Factor)
                criteria[i]["kind"] = st.radio(
                    f"Jenis Kriteria {criteria[i]['name']}",
                    ["CF (Core Factor)", "SF (Secondary Factor)"],
                    key=f"kind_{i}",
                    horizontal=True
                )

            with col2:
                # Tipe data (Scale or Range)
                criteria[i]["type"] = st.selectbox(
                    f"Tipe data dari {criteria[i]['name']}",
                    ["Skala (1-5)", "Range Numerik (e.g. 20-30)"],
                    key=f"type_{i}"
                )

            with col3:
                # Nilai Ideal berdasarkan tipe
                if criteria[i]["type"] == "Skala (1-5)":
                    criteria[i]["ideal"] = st.number_input(
                        f"Nilai Ideal {criteria[i]['name']} (1–5)",
                        min_value=1, max_value=5, value=5, step=1,
                        key=f"ideal_{i}", format="%d"
                    )
                else:
                    criteria[i]["ideal"] = st.number_input(
                        f"Nilai Ideal {criteria[i]['name']}",
                        min_value=0.0, value=0.0, step=0.1,
                        key=f"ideal_{i}"
                    )


        # Pilih metode pembobotan
        st.subheader("Pilih metode pembobotan kriteria:")
        weighting_method = st.radio("", ["Manual", "AHP"], horizontal=True)
        
        if weighting_method == "Manual":
            st.subheader("Input Bobot untuk Setiap Kriteria")
            col1, col2 = st.columns(2)
            weights = []
            
            # Collect weights for all but the last criterion
            for i in range(num_criteria - 1):  # Loop until the second-to-last criterion
                with col1 if i % 2 == 0 else col2:
                    weight = st.number_input(f"Bobot untuk {criteria[i]['name']}", 0.0000, 1.0000, 0.00001, format='%.4f')
                    criteria[i]["weight"] = weight  # Store weight directly in the criteria dictionary
                    weights.append(weight)
            
            # Calculate the weight for the last criterion to ensure the sum is 1
            remaining_weight = 1 - sum(weights)
            criteria[num_criteria - 1]["weight"] = remaining_weight  # Set the weight for the last criterion
            weights.append(remaining_weight)  # Add the last weight to the list

            # Display last weight input dynamically in the correct column
            if (num_criteria - 1) % 2 == 0:  # If it's an even index (for 3 or other odd criteria count)
                with col1:
                    st.number_input(f"Bobot untuk {criteria[num_criteria - 1]['name']}", 
                                    min_value=0.0000, 
                                    max_value=1.0000, 
                                    value=remaining_weight, 
                                    step=0.0001, 
                                    format='%.4f',
                                    key=f"weight_{num_criteria-1}")
            else:
                with col2:
                    st.number_input(f"Bobot untuk {criteria[num_criteria - 1]['name']}", 
                                    value=remaining_weight, format="%.4f", disabled=True,
                                    key=f"weight_{num_criteria-1}")

            # Display the manually set weights, including the calculated last weight
            st.write(f"Bobot Kriteria Manual: {weights}")
        else:  # AHP
            pairwise_matrix = np.ones((num_criteria, num_criteria))

            # Iterate to create pairwise comparisons with slider input
            for i in range(num_criteria):
                for j in range(i + 1, num_criteria):
                    with st.expander(f"🔍✨Bandingkan {criteria[i]['name']} dengan {criteria[j]['name']}"):
                        col1, col2 = st.columns([1, 3])
                        # Radio buttons for selecting which criterion is preferred
                        with col1:
                            higher_priority = st.radio(
                                f"Pilih kriteria yang lebih tinggi antara {criteria[i]['name']} dan {criteria[j]['name']}",
                                options=[criteria[i]['name'], criteria[j]['name']],
                                key=f"priority_criteria_{i}_{j}",
                                horizontal=True
                            )
                        # Slider for scoring with unique key based on i and j
                        with col2:
                            # Teks perbandingan yang dinamis
                            if higher_priority == criteria[i]['name']:
                                comparison_text = f"Seberapa besar {criteria[i]['name']} lebih penting dibandingkan {criteria[j]['name']}"
                            else:
                                comparison_text = f"Seberapa besar {criteria[j]['name']} lebih penting dibandingkan {criteria[i]['name']}"

                            score = st.slider(
                                comparison_text,
                                min_value=1.0,
                                max_value=9.0,
                                value=1.0,
                                step=1.0,
                                key=f"slider_pm_{i}_{j}"  # Unique key for each slider
                            )

                            # Mengubah angka slider menjadi label deskriptif
                            label_dict = {
                                1: "sama penting",
                                2: "mendekati sedikit lebih penting",
                                3: "sedikit lebih penting",
                                4: "mendekati lebih penting",
                                5: "lebih penting dari",
                                6: "mendekati sangat penting",
                                7: "sangat penting",
                                8: "mendekati mutlak",
                                9: "mutlak sangat penting"
                            }
                            
                            selected_label_ahppm = label_dict.get(score, "Unknown")
                            st.write(f"Skor: {selected_label_ahppm}")
                        
                            # Update pairwise matrix based on selection
                            if higher_priority == criteria[i]['name']:
                                pairwise_matrix[i][j] = score
                                pairwise_matrix[j][i] = 1 / score
                            else:
                                pairwise_matrix[j][i] = score
                                pairwise_matrix[i][j] = 1 / score
            
            weights = get_weight(pairwise_matrix, "Kriteria")
            # Store weights in the criteria dictionary
            for i in range(num_criteria):
                criteria[i]["weight"] = weights[i]

            st.write(f"Bobot Kriteria AHP: {weights}")

        # Input skor alternatif untuk Profile Matching
        # Creating a matrix layout for alternatives and their scores
        st.subheader("Input Skor Varietas per Kriteria")
        
        # kita bangun dict scores[alt][kriteria] = single value atau tuple(min,max)
        scores = {}
        for alt in alternatives:
            st.markdown(f"**{alt}**")
            scores[alt] = {}
            # Buat 2 kolom
            col1, col2 = st.columns(2)

            # Looping kriterianya, bagi rata ke kolom 1 dan 2
            for idx, c in enumerate(criteria):
                name = c["name"]

                if c.get("type", "Skala (1-5)") == "Skala (1-5)":
                    # Tentukan mau masuk kolom 1 atau kolom 2
                    target_col = col1 if idx % 2 == 0 else col2

                    with target_col:
                        v = st.number_input(
                            f"Skor {name} untuk {alt}",
                            min_value=1, max_value=5, step=1,
                            key=f"score_{alt}_{name}",
                            format="%d"
                        )
                        scores[alt][name] = v
                else:
                    col1, col2 = st.columns(2)

                    with col1:
                        mn = st.number_input(
                            f"Min {name} untuk {alt}",
                            min_value=0.0, step=0.1,
                            key=f"min_{alt}_{name}"
                        )

                    with col2:
                        mx = st.number_input(
                            f"Max {name} untuk {alt}",
                            min_value=mn, step=0.1,
                            key=f"max_{alt}_{name}"
                        )

                    scores[alt][name] = (mn, mx)

        # ---------- TOMBOL UNTUK MENENTUKAN ALTERNATIF TERBAIK DENGAN PROFILE MATCHING ----------
        if st.button("\U0001F50E Tentukan Varietas Jagung Terbaik dengan Profile Matching"):
            # ---------- CALL PROFILE MATCHING FUNCTION ----------
            result_df = profile_matching(criteria, alternatives, scores)

            # ---------- Menampilkan Hasil Skor dan Ranking Profile Matching ----------
            st.subheader("Hasil Ranking Varietas Berdasarkan Profile Matching")
            st.dataframe(result_df, use_container_width=True, hide_index=True)
            # reset index agar 0,1,2… secara berurutan
            result_df = result_df.reset_index(drop=True)

            best_choice_name = result_df.loc[0, "Varietas"]
            best_score      = result_df.loc[0, "Total Score"]
            st.success(f"Varietas terbaik adalah **{best_choice_name}** dengan skor {best_score:.4f}.")
            st.markdown(f"""
            ### \U0001F4DD Kesimpulan
            Berdasarkan hasil perhitungan dengan metode Profile Matching, varietas **{best_choice_name}** merupakan pilihan terbaik
            karena memiliki skor total tertinggi. Varietas ini diharapkan memberikan hasil paling optimal berdasarkan kriteria yang telah ditentukan.""")
    elif method is None:
        st.write("**Silakan pilih metode pengambilan keputusan yang akan digunakan.**")

if __name__ == '__main__':
    main()

#Import Packages
import streamlit as st
import numpy_financial as npf



#Metadata
favicon = "images/mandiri_logo.jpg"
st.set_page_config(page_title="Kalkulator KUR Bank Mandiri", page_icon=favicon, layout="centered", initial_sidebar_state = "auto")


#Header
header_image = "images/header.png" 
st.image(header_image)

st.markdown('##')

#Input
number = st.number_input('Jumlah Kredit Yang Ingin Diajukan',
                         value = 10000000,
                         min_value = 1000000, 
                         max_value = 350000000,
                         format = None)
st.caption("Total Pinjaman:   Rp " +"{:,.2f}".format(number))
st.markdown('#')

slider_month = st.slider('Tenor Pinjaman (Dalam Bulan)', 
                         min_value = 12,
                         max_value = 60,
                         step = 12)

st.caption("Durasi Pinjaman:    " + str(slider_month) + " bulan")


#Define variables
principal = number
effective_rate = 0.06
term_month = slider_month

#Calculation
calculation = npf.pmt(effective_rate / 12, term_month,  principal)* - 1
output_unformatted = "{:,.2f}".format(calculation)
output = "Rp " + output_unformatted


#Output
st.markdown('##')
with st.container():
    st.subheader("Angsuran yang Dibayar per Bulan")
    st.info(output)

#Button    
url = "'https://api.whatsapp.com/send?phone=6282319751963&text=Halo!%20Saya%20ingin%20mengajukan%20KUR%20dari%20Bank%20Mandiri'"

st.markdown('##')

st.markdown(f'''
<a href={url}><button style=
"
color: #ffffff;
background-color: #2d63c8;
font-size: 19px;
border: 1px solid #2d63c8;
border-radius: 11px;
padding: 15px 50px;
cursor: pointer;
width: 100%
" 
type="button" name="">Ajukan Kredit</button></a>
''',
unsafe_allow_html=True)

#Footer
st.markdown('##')
st.markdown('##')
st.image("images/kur_footer.png")


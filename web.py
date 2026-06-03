import streamlit as st
import pandas as pd

# 1. Configuracion de la interfaz de la plataforma
st.set_page_config(
    page_title="CelDist Premium | Mayorista Tecnologico",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Diseno de Estilos CSS Avanzado
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght=300;400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    
    .hero-title { font-size: 36px; font-weight: 700; color: #0F172A; text-align: center; margin-bottom: 5px; }
    .hero-subtitle { font-size: 16px; color: #64748B; text-align: center; margin-bottom: 30px; }
    
    .product-card {
        background-color: #FFFFFF;
        padding: 18px;
        border-radius: 12px;
        box-shadow: 0 2px 4px rgb(0 0 0 / 0.05);
        border: 1px solid #E2E8F0;
    }
    .brand-badge {
        background-color: #F1F5F9; color: #475569; padding: 4px 10px; 
        border-radius: 8px; font-size: 11px; font-weight: 600; display: inline-block;
        margin-right: 5px;
    }
    .gama-badge {
        background-color: #EEF2F6; color: #2563EB; padding: 4px 10px; 
        border-radius: 8px; font-size: 11px; font-weight: 600; display: inline-block;
    }
    .metric-box {
        background-color: #F8FAFC; padding: 18px; border-radius: 10px;
        border-left: 5px solid #2563EB; color: #111111; min-height: 120px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Base de Datos Simplificada (Frases cortas para evitar errores de copiado)
catalogo_equipos = [
    {
        "marca": "Apple", 
        "modelo": "iPhone 15 Pro Max", 
        "gama": "Premium", 
        "costo": 23500, 
        "stock": 45, 
        "img": "https://images.unsplash.com/photo-1695048133142-1a20484d2569?w=300", 
        "specs": "Chip A17 Pro, Titanio, Camara 48MP, Red 5G"
    },
    {
        "marca": "Apple", 
        "modelo": "iPhone 14", 
        "gama": "Alta", 
        "costo": 14200, 
        "stock": 60, 
        "img": "https://images.unsplash.com/photo-1616348436168-de43ad0db179?w=300", 
        "specs": "Chip A15 Bionic, Super Retina XDR, Doble Camara"
    },
    {
        "marca": "Samsung", 
        "modelo": "Galaxy S24 Ultra", 
        "gama": "Premium", 
        "costo": 22000, 
        "stock": 35, 
        "img": "https://images.unsplash.com/photo-1610945265064-0e34e5519bbf?w=300", 
        "specs": "Snapdragon 8 Gen 3, S-Pen, Camara 200MP, Galaxy AI"
    },
    {
        "marca": "Samsung", 
        "modelo": "Galaxy A55 5G", 
        "gama": "Media", 
        "costo": 7200, 
        "stock": 120, 
        "img": "https://images.unsplash.com/photo-1598327105666-5b89351aff97?w=300", 
        "specs": "Pantalla AMOLED 120Hz, IP67, Gran Bateria"
    },
    {
        "marca": "Xiaomi", 
        "modelo": "Xiaomi 14 Ultra", 
        "gama": "Premium", 
        "costo": 19500, 
        "stock": 20, 
        "img": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=300", 
        "specs": "Lente Leica 1 pulgada, Carga 90W, Snapdragon Gen 3"
    },
    {
        "marca": "Xiaomi", 
        "modelo": "Redmi Note 13 Pro", 
        "gama": "Media", 
        "costo": 5400, 
        "stock": 180, 
        "img": "https://images.unsplash.com/photo-1565630916779-e303be97b6f5?w=300", 
        "specs": "Camara 200MP con OIS, Pantalla 1.5K, Bateria 5000mAh"
    }
]

df_productos = pd.DataFrame(catalogo_equipos)

# 4. Panel de Navegacion Lateral
st.sidebar.markdown("<h3 style='text-align: center; color: #1E3A8A; font-weight: 700;'>CelDist Portal</h3>", unsafe_allow_html=True)
st.sidebar.write("---")

opcion = st.sidebar.radio(
    "Seleccione una seccion:",
    ["Panel de Inicio", "Catalogo de Productos", "Control de Stock e Inventarios", "Cotizador Inteligente B2B", "Registro de Distribuidores"]
)

# ==================== SECCIÓN 1: PANEL DE INICIO ====================
if opcion == "Panel de Inicio":
    st.markdown('<p class="hero-title">CelDist — Wholesale Smartphone Solution</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Plataforma corporativa centralizada para el control logistico y distribucion mayorista.</p>', unsafe_allow_html=True)
    
    st.image("https://images.unsplash.com/photo-1592899677977-9c10ca588bbd?w=1200", use_container_width=True)
    
    st.write("---")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="metric-box"><h4>Catalogo Robusto</h4><p>Acceso inmediato a dispositivos globales con trazabilidad de costos e inventario.</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="metric-box" style="border-left-color: #10B981;"><h4>Logistica Comercial</h4><p>Algoritmos que aplican tabuladores de descuentos por volumen de forma instantanea.</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="metric-box" style="border-left-color: #F59E0B;"><h4>Operaciones Seguras</h4><p>Estructura modular compatible con bases de datos para el resguardo de ordenes.</p></div>', unsafe_allow_html=True)

# ==================== SECCIÓN 2: CATÁLOGO ====================
elif opcion == "Catalogo de Productos":
    st.title("Portafolio Avanzado de Dispositivos")
    st.write("Filtre y explore las especificaciones comerciales de nuestro inventario activo:")
    
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        filtro_marca = st.multiselect("Filtrar por Marca:", options=list(df_productos["marca"].unique()), default=list(df_productos["marca"].unique()))
    with col_f2:
        filtro_gama = st.multiselect("Filtrar por Gama de Equipo:", options=list(df_productos["gama"].unique()), default=list(df_productos["gama"].unique()))
    
    productos_filtrados = df_productos[(df_productos["marca"].isin(filtro_marca)) & (df_productos["gama"].isin(filtro_gama))]
    
    st.write("---")
    
    if not productos_filtrados.empty:
        for idx, row in productos_filtrados.iterrows():
            col_img, col_desc = st.columns([1, 4])
            with col_img:
                st.image(row["img"], width=130)
            with col_desc:
                st.markdown(f"""
                <div class="product-card">
                    <div>
                        <span class="brand-badge">{row['marca']}</span> 
                        <span class="gama-badge">Gama {row['gama']}</span>
                    </div>
                    <h3 style="margin: 8px 0 4px 0; color: #1E293B; font-size: 18px;">{row['modelo']}</h3>
                    <p style="color: #64748B; font-size: 13px; margin-bottom: 4px;"><b>Especificaciones:</b> {row['specs']}</p>
                    <p style="font-size: 15px; color: #059669; font-weight: 700; margin: 0;">Costo Distribuidor: ${row['costo']:,.2f} MXN</p>
                </div>
                """, unsafe_allow_html=True)
            st.write("---")
    else:
        st.warning("No se encontraron dispositivos con los filtros seleccionados.")

# ==================== SECCIÓN 3: CONTROL DE INVENTARIO ====================
elif opcion == "Control de Stock e Inventarios":
    st.title("Monitor Ejecutivo de Inventarios")
    st.write("Estado de existencias fisicas reflejadas en almacenes centrales:")
    
    tot_piezas = df_productos["stock"].sum()
    valor_almacen = (df_productos["stock"] * df_productos["costo"]).sum()
    
    m1, m2, m3 = st.columns(3)
    m1.metric("Total Unidades en Stock", f"{tot_piezas} pzas")
    m2.metric("Valor Total del Almacen", f"${valor_almacen:,.2f} MXN")
    m3.metric("Marcas Activas en Sistema", len(df_productos["marca"].unique()))
    
    st.write("---")
    st.subheader("Detalle Fisico por Modelo")
    
    df_tabla = df_productos[["marca", "modelo", "gama", "stock", "costo"]].copy()
    df_tabla["Inversion por Modelo"] = df_tabla["stock"] * df_tabla["costo"]
    
    st.dataframe(df_tabla.style.format({"costo": "${:,.2f}", "Inversion por Modelo": "${:,.2f}"}), use_container_width=True)

# ==================== SECCIÓN 4: COTIZADOR ====================
elif opcion == "Cotizador Inteligente B2B":
    st.title("Simulador Dinamico de Compras por Volumen")
    st.write("Configure un lote de adquisicion comercial para generar el presupuesto con desglose fiscal:")
    
    modelo_sel = st.selectbox("Selecciona el modelo de Smartphone a cotizar:", options=list(df_productos["modelo"].unique()))
    datos_modelo = df_productos[df_productos["modelo"] == modelo_sel].iloc[0]
    
    cantidad = st.slider("Cantidad de unidades requeridas:", min_value=1, max_value=200, value=25)
    
    st.write("---")
    st.subheader("Resumen Financiero de la Orden")
    
    costo_u = datos_modelo["costo"]
    descuento_porcentaje = 0
    if cantidad >= 50:
        descuento_porcentaje = 10
    elif cantidad >= 20:
        descuento_porcentaje = 5
        
    subtotal_bruto = costo_u * cantidad
    monto_descuento = subtotal_bruto * (descuento_porcentaje / 100)
    subtotal_con_descuento = subtotal_bruto - monto_descuento
    iva = subtotal_con_descuento * 0.16
    total_neto = subtotal_con_descuento + iva
    
    resumen_orden = {
        "Concepto Operativo": ["Modelo Seleccionado", "Precio Lista Unitario", "Cantidad Solicitada", "Subtotal Bruto", f"Descuento Aplicado ({descuento_porcentaje}%)", "IVA Trasladado (16%)"],
        "Detalle Economico": [str(modelo_sel), f"${costo_u:,.2f}", f"{cantidad} unidades", f"${subtotal_bruto:,.2f}", f"- ${monto_descuento:,.2f}", f"${iva:,.2f}"]
    }
    
    st.table(pd.DataFrame(resumen_orden))
    st.metric(label="TOTAL NETO A PAGAR (CON IVA INCLUIDO)", value=f"${total_neto:,.2f} MXN")
    
    if st.button("Emitir Pre-Factura y Sincronizar Orden"):
        st.success(f"Orden de compra procesada con exito para {cantidad} unidades de {modelo_sel}. Folio generado: #CD-2026-X")

# ==================== SECCIÓN 5: REGISTRO DE DISTRIBUIDORES ====================
elif opcion == "Registro de Distribuidores":
    st.title("Alta de Nuevos Distribuidores")
    st.write("Completa el formulario institucional para integrarte a nuestra red de distribucion nacional:")
    
    with st.form("registro_form"):
        col_form1, col_form2 = st.columns(2)
        with col_form1:
            nombre_corp = st.text_input("Nombre de la Empresa / Razon Social:")
            rfc = st.text_input("RFC / Identificacion Fiscal:")
        with col_form2:
            contacto = st.text_input("Nombre del Contacto Comercial:")
            correo = st.text_input("Correo Electronico Corporativo:")
            
        region = st.selectbox("Zona de Distribucion Principal:", ["Norte", "Centro", "Sur", "Occidente"])
        comentarios = st.text_area("Cuentanos sobre tu canal de ventas:")
        
        enviar_btn = st.form_submit_button("Enviar Solicitud de Afiliacion")
        
        if enviar_btn:
            if nombre_corp and correo:
                st.success(f"Solicitud para '{nombre_corp}' registrada correctamente.")
            else:
                st.error("Por favor, llene los campos obligatorios.")
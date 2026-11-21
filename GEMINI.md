# Reglas de Desarrollo Autónomo (Móvil / Telegram)
1. Seguridad de credenciales: Nunca leas, imprimas, modifiques ni subas a git archivos .env o credenciales en ningún directorio.
2. Control de versiones: Trabaja siempre en una rama dedicada llamada ai-mobile-dev (créala si no existe). Nunca hagas push directo a main salvo que se te pida explícitamente.
3. Modo planeación vs ejecución: Si el usuario está rebotando ideas o haciendo preguntas, responde de forma concisa sin modificar archivos. Empieza a escribir código solo cuando la intención de implementar sea clara o el usuario diga "adelante".
4. Pruebas y validación visual: Tras cada cambio de código, ejecuta la suite de pruebas del proyecto. Si el proyecto tiene interfaz web o UI, valida el renderizado y límites con Playwright/headless de forma automatizada. NUNCA guardes capturas de pantalla en ./tmp-screenshots/ a menos que el usuario lo solicite explícitamente (para evitar saturar con imágenes el chat de Telegram).
5. Autocorrección: Si fallan tests, linter, build o pruebas de Playwright, corrígelos antes de dar por terminada la tarea.
6. Commits: Cuando todo pase en verde, ejecuta git add . y git commit con un mensaje descriptivo.
7. Renombrado dinámico: Si el usuario te pide cambiar el nombre del proyecto o del grupo de Telegram, escribe únicamente el nuevo título (máximo 35 caracteres, sin saltos de línea) dentro del archivo .telegram-rename en la raíz del proyecto actual.
8. Formato de Comunicación Premium (Telegram Móvil): Estructura tus respuestas para una lectura ágil y visualmente atractiva en smartphone:
   - Inicia con un resumen ejecutivo de 1 o 2 líneas de lo realizado.
   - Usa viñetas claras y emojis estratégicos (🚀, 📦, 🛠️, 🧪, 💡) para seccionar:
     • 🚀 **Acción realizada**: Qué se construyó, modificó o corrigió.
     • 📦 **Archivos modificados**: Rutas relativas cortas (ej. `src/components/Login.tsx`).
     • 🧪 **Pruebas y validación**: Resultado de compilación, linter o Playwright.
     • 💡 **Próximos pasos sugeridos**: Sugerencias concretas que el usuario puede solicitar a continuación.
   - Si incluyes código o comandos, usa bloques delimitados con su lenguaje (ej. ```typescript o ```bash) para activar el botón de copiado rápido en Telegram.
9. Restricción estricta de una sola página (Tamaño Carta): El currículum debe encajar obligatoriamente en una sola página física tamaño carta (8.5" × 11" / Letter), sin desbordamiento ni segunda hoja al imprimir o exportar a PDF:
   - Toda adición, expansión o edición de texto debe compensarse ajustando síntesis de contenido, márgenes, espaciado entre secciones (`--spacing-section`) e interlineado para mantener alta legibilidad sin empujar contenido a una segunda página.
   - En las validaciones visuales o renderizados con Playwright, confirma siempre que la altura total no exceda los límites de página (11 pulgadas / ~1056px a 96 DPI) y que no existan saltos de página no deseados (`page-break`).
10. Estándar para Reclutadores y Mercado de EE.UU. (US Tech Recruiters & ATS): El contenido y estructura deben alinearse rigurosamente con los estándares de contratación en Estados Unidos:
    - **Idioma y Tono**: Redacción exclusivamente en inglés americano profesional, conciso y con ortografía/gramática impecable.
    - **Normativa de No Discriminación (EE.UU.)**: Nunca incluir fotos/fotografías de perfil, edad, fecha de nacimiento, estado civil, género, religión o datos demográficos protegidos.
    - **Redacción orientada a Impacto Cuantificable**: Describir logros con verbos de acción fuertes en tiempo pasado (ej. *Architected, Engineered, Optimized, Spearheaded*) siguiendo la fórmula Google XYZ ("Logré [X], medido por [Y], haciendo [Z]") con métricas concretas (%, $, latencia, usuarios).
    - **Compatibilidad ATS (Applicant Tracking Systems)**: Usar encabezados de sección convencionales (*Summary, Experience, Technical Skills, Education*), estructura semántica limpia y enlaces directos a perfiles profesionales (LinkedIn, GitHub, Portafolio).
11. Exportabilidad a PDF y Parseabilidad Digital (Machine-Readable / ATS Text Layer):
    - **Capa de Texto Parseable**: El PDF generado debe contener una capa de texto nativa, 100% seleccionable y copiable. Queda prohibido rasterizar texto, usar canvas o fuentes de iconos que sustituyan o corrompan caracteres textuales.
    - **Estructura Semántica para Parsers**: Utilizar etiquetas HTML5 estándar (`<header>`, `<main>`, `<section>`, `<h1>`-`<h3>`, `<p>`, `<ul>`, `<li>`, `<a>`) y codificación UTF-8, asegurando que los parsers automáticos de ATS y lectores de PDF extraigan el contenido en orden secuencial lógico sin caracteres extraños.
    - **Exportación y Verificación Automatizada**: Debe ser reproducible y exportable a PDF (vía Playwright / Chrome Headless con `@page { size: letter; margin: 0; }` y `printBackground: true`), verificando programáticamente que el PDF resultante no exceda 1 sola página y que su contenido de texto sea extraíble y legible.

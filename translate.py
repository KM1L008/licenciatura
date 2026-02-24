import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

replacements = [
    # Topbar
    (r'<!-- ===== TOP BAR ===== -->[\s\S]*?<!-- ===== NAVBAR ===== -->', '<!-- ===== NAVBAR ===== -->'),
    # Nav
    (r'>Home<', '>Inicio<'),
    (r'>About<', '>Nosotros<'),
    (r'>Classes<', '>Clases<'),
    (r'>Events<', '>Eventos<'),
    (r'>Teacher<', '>Maestros<'),
    (r'>Programs<', '>Programas<'),
    (r'>Blog<', '>Blog<'),
    
    # Hero
    (r'Kindori Kindergarten School', 'Escuela Infantil Kindori'),
    (r'A Brighter Future<br />For All.', 'Un Futuro Brillante<br />Para Todos.'),
    (r'The Universe is one great kindergarten for man\. Everything that\s+exists has brought with it its own peculiar lesson\.', 'El universo es un gran jardín de infancia para el hombre. Todo lo que\\n            existe ha traído consigo su propia lección peculiar.'),
    (r'>Discover More<', '>Descubrir Más<'),
    (r'>Happy Kids<', '>Niños Felices<'),
    
    # Values
    (r'>WHY CHOOSE US<', '>POR QUÉ ELEGIRNOS<'),
    (r'>Our Core Values<', '>Nuestros Valores Principales<'),
    (r'With kindori, we always put the quality of teaching children first,\s+please rest assured when sending children at kindori kindergarten\.', 'En Kindori, siempre ponemos la calidad de la enseñanza de los niños en primer lugar,\\n          siéntase seguro al enviar a sus hijos a nuestra escuela.'),
    (r'>Learn And Play<', '>Aprende y Juega<'),
    (r'With the scheme of playing and learning together, children will\s+have a comfortable experience\.', 'Con el esquema de jugar y aprender juntos, los niños tendrán una\\n              experiencia cómoda.'),
    (r'>Nutritious Meal<', '>Comida Nutritiva<'),
    (r'Children\'s needs need to be provided with all the nutrients\s+necessary for a day of play\.', 'Las necesidades de los niños requieren de todos los nutrientes\\n              necesarios para un día de juego.'),
    (r'>Great Teachers<', '>Grandes Maestros<'),
    (r'Experienced and dedicated teachers team will help your child\s+develop more in all aspects\.', 'Un equipo de maestros experimentados y dedicados ayudará a su hijo a\\n              desarrollarse más en todos los aspectos.'),
    (r'>Cute Environment<', '>Ambiente Agradable<'),
    (r'The colorful environment at Kindori is suitable for children\'s\s+age, making them more accessible\.', 'El ambiente colorido en Kindori es adecuado para la edad de los niños,\\n              haciéndolo más accesible.'),
    
    # Enroll
    (r'<span class="pink">How To</span> Let Your Child Study At Kindori\?', '<span class="pink">¿Cómo</span> Inscribir a su Hijo en Kindori?'),
    (r'Let your child attend Kindori Kindergarten to help your child\s+develop comprehensively in all aspects\.', 'Deje que su hijo asista a la Escuela Infantil Kindori para ayudarle a\\n            desarrollarse integralmente en todos los aspectos.'),
    (r'>Enrollment Now!<', '>¡Inscríbete Ahora!<'),
    
    # Guiding
    (r'Guiding The Young Generation<br /><span class="dark"\s+>To Success\.</span\s+>', 'Guiando a la Joven Generación<br /><span class="dark"\\n              >al Éxito.</span\\n            >'),
    (r'At Kindori, we believe every child holds a universe of\s+possibilities\. Our experienced educators nurture curiosity,\s+creativity, and confidence from the very first day, building a\s+strong foundation for a lifetime of learning\.', 'En Kindori, creemos que cada niño alberga un universo de posibilidades. Nuestros educadores experimentados fomentan la curiosidad, la creatividad y la confianza desde el primer día, construyendo una base sólida para una vida de aprendizaje.'),
    (r'> Child-centered learning\s+approach', '> Enfoque de aprendizaje centrado en el niño'),
    (r'> Safe and stimulating\s+environment', '> Entorno seguro y estimulante'),
    (r'> Qualified and caring staff', '> Personal cualificado y atento'),
    (r'> Holistic developmental\s+programs', '> Programas de desarrollo holístico'),
    (r'>Learn More<', '>Saber Más<'),
    
    # Classes
    (r'>OUR CLASSES<', '>NUESTRAS CLASES<'),
    (r'>Special Classes For Kids<', '>Clases Especiales Para Niños<'),
    (r'We offer a variety of specially designed classes to bring out the best\s+in every child\.', 'Ofrecemos una variedad de clases especialmente diseñadas para sacar lo mejor de cada niño.'),
    (r'>Art & Craft<', '>Arte y Manualidades<'),
    (r'Creative expression through drawing, painting, and crafting\s+projects\.', 'Expresión creativa a través del dibujo, la pintura y proyectos de\\n              manualidades.'),
    (r'Age: 3 – 5 yrs', 'Edad: 3 – 5 años'),
    
    (r'>Music & Dance<', '>Música y Danza<'),
    (r'Rhythmic activities that develop coordination and express\s+emotions\.', 'Actividades rítmicas que desarrollan la coordinación y expresan\\n              emociones.'),
    (r'Age: 3 – 6 yrs', 'Edad: 3 – 6 años'),
    
    (r'>Little Scientists<', '>Pequeños Científicos<'),
    (r'Fun science experiments that spark curiosity about how the world\s+works\.', 'Divertidos experimentos científicos que despiertan la curiosidad sobre cómo funciona\\n              el mundo.'),
    (r'Age: 4 – 6 yrs', 'Edad: 4 – 6 años'),
    
    (r'>Sports & Fitness<', '>Deportes y Ejercicio<'),
    (r'Active play and exercise programs to promote healthy development\.', 'Juegos activos y programas de ejercicio para promover un desarrollo saludable.'),
    
    (r'>Reading & Writing<', '>Lectura y Escritura<'),
    (r'Early literacy building blocks that set the stage for academic\s+success\.', 'Bases iniciales de alfabetización que preparan el escenario para el éxito\\n              académico.'),
    
    (r'>Nature Explorers<', '>Exploradores de la Naturaleza<'),
    (r'Outdoor exploration that builds environmental awareness and\s+wonder\.', 'Exploración al aire libre que fomenta la conciencia ambiental y el\\n              asombro.'),
    
    # Teachers
    (r'>OUR TEAM<', '>NUESTRO EQUIPO<'),
    (r'>Meet Our Teachers<', '>Conoce a Nuestros Maestros<'),
    (r'Our dedicated team of educators is passionate about shaping young\s+minds with love and creativity\.', 'Nuestro dedicado equipo de educadores siente pasión por formar mentes jóvenes\\n          con amor y creatividad.'),
    (r'>Head Teacher<', '>Maestra Principal<'),
    (r'>Arts Teacher<', '>Maestra de Arte<'),
    (r'>Music Teacher<', '>Maestro de Música<'),
    (r'>Science Teacher<', '>Maestra de Ciencias<'),
    
    # Blog
    (r'>LATEST NEWS<', '>ÚLTIMAS NOTICIAS<'),
    (r'>From Our Blog<', '>De Nuestro Blog<'),
    (r'Stay up to date with the latest news, tips and activities from Kindori\s+Kindergarten\.', 'Manténgase al día con las últimas noticias, consejos y actividades de la Escuela Infantil\\n          Kindori.'),
    (r'>Education<', '>Educación<'),
    (r'>10 Fun Learning Activities for Toddlers at Home<', '>10 Actividades de Aprendizaje Divertidas para los Pequeños en Casa<'),
    (r'Discover creative and engaging activities you can do with your\s+little ones to stimulate their development every day\.', 'Descubre actividades creativas y atractivas que puedes hacer con tus\\n                pequeños para estimular su desarrollo cada día.'),
    (r'Read More ', 'Leer Más '),
    
    (r'>Nutrition<', '>Nutrición<'),
    (r'>Healthy Lunch Box Ideas for Your Kindergartner<', '>Ideas de Loncheras Saludables para su Hijo<'),
    (r'Simple, nutritious and colorful meal ideas that your children\s+will love and that give them energy to learn\.', 'Ideas de comidas sencillas, nutritivas y coloridas que a tus niños\\n                les encantarán y les darán energía para aprender.'),
    
    (r'>Tips<', '>Consejos<'),
    (r'>Preparing Your Child for the First Day of School<', '>Preparando a su Hijo para el Primer Día de Clases<'),
    (r'Practical tips and emotional strategies to help your little one\s+feel confident and excited about school\.', 'Consejos prácticos y estrategias emocionales para ayudar a su pequeño a\\n                sentirse seguro y emocionado por la escuela.'),
    
    # Footer
    (r'Providing quality early childhood education and a nurturing\s+environment where every child can thrive and grow\.', 'Proporcionando una educación infantil de calidad y un entorno enriquecedor\\n            donde cada niño puede prosperar y crecer.'),
    (r'>Quick Links<', '>Enlaces Rápidos<'),
    (r'>About Us<', '>Sobre Nosotros<'),
    (r'>Contact Us<', '>Contáctanos<'),
    (r'>Art &amp; Craft<', '>Arte y Manualidades<'),
    (r'>Music &amp; Dance<', '>Música y Danza<'),
    (r'>Little Scientists<', '>Pequeños Científicos<'),
    (r'>Sports &amp; Fitness<', '>Deportes y Ejercicio<'),
    (r'>Nature Explorers<', '>Exploradores de la Naturaleza<'),
    (r'Mon–Sat 8am – 5pm', 'Lun-Sáb 8am - 5pm'),
    (r'All rights reserved\. Designed\s+with', 'Todos los derechos reservados. Diseñado\\n          con'),
]

for pat, repl in replacements:
    html = re.sub(pat, repl, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

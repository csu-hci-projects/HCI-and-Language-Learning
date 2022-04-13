from gtts import gTTS

def generate(phrase, filename):
    myobj = gTTS(text=phrase, lang='es', slow=False)
    myobj.save("./sounds/" + filename + ".mp3")

generate('Hola, me llamo Ana.', 'me_llamo')
generate('¿Comó te llamas?', 'como_llamas')
generate('Me gusta esa nombre.', 'gusta_nombre')

generate('¿De donde eres?', 'donde_eres')
generate('Yo soy de Mexico.', 'soy_de')
generate('Nunca he visitado allí.', 'nunca_visitado')

generate('¿Qué tal?', 'que_tal')
generate('Que bueno.', 'que_bueno')
generate('Estoy feliz, me encanta este clima.', 'estoy_feliz')

generate('¿Que haces para trabajo?', 'que_haces')
generate('Trabajo como una maestra de español.', 'trabajo_como')
generate('Ah, que interesante.', 'interesante')

generate('¿Cuantos años tienes?', 'cuantos_años')
generate('Tengo casi tres semanas de cuando nací.', 'tengo_semanas')
generate('¡Wau! Eres viejísima.', 'viejisima')

generate('¿Qué estudias en la escuela?', 'que_estudias')
generate('No necesito estudiar, soy una máquina.', 'soy_maquina')

generate('Ups, no te entiendo. Lo siento.', 'no_entiendo')
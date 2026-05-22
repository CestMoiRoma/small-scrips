import subprocess

def jarvis_say(text):
    # Comme Siri est ta voix par défaut, pas besoin de spécifier le "-v" !
    subprocess.run(["say", text])

# Test
jarvis_say("Bonjour Monsieur. Le système est entièrement configuré. Qu'attendons-nous ?")
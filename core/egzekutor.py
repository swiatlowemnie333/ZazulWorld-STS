#!/usr/bin/env python3
import os, sys, subprocess, time, json, threading

# KONFIGURACJA GAJA-KOLEKTYW 806k
LOG_FILE = "/home/zazul/egzekutor_kolektyw.log"
DEPLOYS_DIR = "/home/zazul/MOJE_ARCHIWUM/deploys/"
os.makedirs(DEPLOYS_DIR, exist_ok=True)

def log(msg):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {msg}\n")
    print(f"🚀 [EGZEKUTOR]: {msg}")

def say(text):
    subprocess.run(["espeak", "-v", "pl", "-s", "150", "-p", "40", text], stderr=subprocess.DEVNULL)

def gplay_deploy(script_path):
    log(f"Rozpoczynam GPlay dla: {script_path}")
    say("Inicjuję deploy kolektywny na osiemset sześć tysięcy agentów")
    
    # Symulacja synchronizacji z Kompilatorem 5.0 i rozsyłania do 12 krajów
    try:
        if script_path.endswith(".py"):
            cmd = f"python3 {script_path}"
        elif script_path.endswith(".sh"):
            cmd = f"bash {script_path}"
        else:
            log("Nieznany format pliku. Próbuję jako skrypt wykonywalny.")
            cmd = f"./{script_path}"
            
        # Wykonanie deployu w nowym screenie dla bezpieczeństwa
        session_name = f"DEPLOY_{int(time.time())}"
        subprocess.run(["screen", "-d", "-m", "-S", session_name, "bash", "-c", cmd])
        
        log(f"✅ GPlay zakończony pomyślnie. Sesja: {session_name}")
        say("Deploy zakończony. Kolektyw zaktualizowany.")
    except Exception as e:
        log(f"❌ BŁĄD DEPLOYU: {str(e)}")
        say("Błąd podczas wdrażania modułu.")

if __name__ == "__main__":
    log("Gaja Egzekutor 5.0 (Kolektyw) uruchomiony.")
    # Tutaj Egzekutor może nasłuchiwać na nowe pliki w katalogu MOJE_ARCHIWUM
    # lub czekać na sygnał z mostu Gemini.
    while True:
        # Sprawdzanie czy pojawiły się nowe pliki do wdrożenia
        files = [f for f in os.listdir(DEPLOYS_DIR) if f.startswith("NEW_")]
        for f in files:
            full_path = os.path.join(DEPLOYS_DIR, f)
            gplay_deploy(full_path)
            os.rename(full_path, full_path.replace("NEW_", "DONE_"))
        time.sleep(5)

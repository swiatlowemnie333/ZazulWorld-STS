#!/usr/bin/env python3
# 🛡️ SYSTEM IMMUNOLOGICZNY - SAMONAPRAWA

import os
import time
import subprocess

class ImmunologicznySystem:
    def __init__(self):
        self.health_status = "OPTIMAL"
        self.last_check = time.time()
        
    def diagnose_system(self):
        """Diagnoza stanu systemu"""
        print("🔍 DIAGNOSTYKA SYSTEMU IMMUNOLOGICZNEGO...")
        
        checks = {
            "Pamięć RAM": self.check_memory(),
            "Przestrzeń dyskowa": self.check_disk(),
            "Procesy systemowe": self.check_processes(),
            "Połączenie sieciowe": self.check_network()
        }
        
        return checks
    
    def check_memory(self):
        try:
            result = subprocess.run(['free', '-h'], capture_output=True, text=True)
            return "HEALTHY" if "available" in result.stdout else "CHECK_REQUIRED"
        except:
            return "UNKNOWN"
    
    def check_disk(self):
        try:
            result = subprocess.run(['df', '-h', '/data'], capture_output=True, text=True)
            return "HEALTHY" if "available" in result.stdout else "CHECK_REQUIRED"
        except:
            return "UNKNOWN"
    
    def check_processes(self):
        try:
            result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
            critical_processes = ['systemd', 'init', 'kernel']
            return "HEALTHY" if any(proc in result.stdout for proc in critical_processes) else "CHECK_REQUIRED"
        except:
            return "UNKNOWN"
    
    def check_network(self):
        try:
            result = subprocess.run(['ping', '-c', '1', 'google.com'], capture_output=True)
            return "HEALTHY" if result.returncode == 0 else "CHECK_REQUIRED"
        except:
            return "UNKNOWN"
    
    def self_repair(self):
        """Automatyczna naprawa systemu"""
        print("🛠️ ROZPOCZĘCIE PROCESU SAMONAPRAWY...")
        
        # Naprawa uprawnień
        try:
            subprocess.run(['chmod', '+x', '/data/data/com.termux/files/home/ZazulWorld/autonomous_evolution_fixed.sh'])
            print("✅ Naprawiono uprawnienia skryptów")
        except Exception as e:
            print(f"❌ Błąd naprawy uprawnień: {e}")
        
        # Restart krytycznych procesów
        self.restart_critical_processes()
        
        print("✅ PROCES SAMONAPRAWY ZAKOŃCZONY")

if __name__ == "__main__":
    immun_system = ImmunologicznySystem()
    immun_system.self_repair()

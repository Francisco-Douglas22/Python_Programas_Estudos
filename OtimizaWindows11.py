import os

# Desativar serviços desnecessários
os.system('services.msc')

# Limpar o disco
os.system('cleanmgr')

# Desfragmentar o disco
os.system('defrag c:')

print("Otimização concluída!")
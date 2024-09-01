import winreg as reg
import os

key_path = r"AppEvents\Schemes\Apps\.Default\DeviceConnect\.Current"
new_sound_path = r"C:\Users\Public.DESKTOP-F6CJGT8\Desktop\bye.wav"

hkeys = [
r"HKEY_CURRENT_USER\AppEvents\Schemes\Apps\.Default\WindowsLogon\.Current",
r"HKEY_CURRENT_USER\AppEvents\Schemes\Apps\.Default\WindowsLogoff\.Current",
r"HKEY_CURRENT_USER\AppEvents\Schemes\Apps\.Default\WindowsUnlock\.Current",
r"HKEY_CURRENT_USER\AppEvents\Schemes\Apps\.Default\SystemCritical\.Current",
r"HKEY_CURRENT_USER\AppEvents\Schemes\Apps\.Default\.Default\.Current",
r"HKEY_CURRENT_USER\AppEvents\Schemes\Apps\.Default\SystemExclamation\.Current",
r"HKEY_CURRENT_USER\AppEvents\Schemes\Apps\.Default\SystemAsterisk\.Current",
r"HKEY_CURRENT_USER\AppEvents\Schemes\Apps\.Default\SystemNotification\.Current",
r"HKEY_CURRENT_USER\AppEvents\Schemes\Apps\.Default\SystemHand\.Current",
r"HKEY_CURRENT_USER\AppEvents\Schemes\Apps\.Default\EmptyRecycleBin\.Current",
r"HKEY_CURRENT_USER\AppEvents\Schemes\Apps\.Default\Notification.Looping.Alarm\.Current",
r"HKEY_CURRENT_USER\AppEvents\Schemes\Apps\.Default\DeviceConnect\.Current",
r"HKEY_CURRENT_USER\AppEvents\Schemes\Apps\.Default\DeviceDisconnect\.Current",
r"HKEY_CURRENT_USER\AppEvents\Schemes\Apps\.Default\LowBatteryAlarm\.Current",
r"HKEY_CURRENT_USER\AppEvents\Schemes\Apps\.Default\BatteryLow\.Current",
r"HKEY_CURRENT_USER\AppEvents\Schemes\Apps\.Default\SystemExit\.Current",
r"HKEY_CURRENT_USER\AppEvents\Schemes\Apps\.Default\WindowsUAC\.Current",
r"HKEY_CURRENT_USER\AppEvents\Schemes\Apps\.Default\SystemNotification\.Current"]

for i in range (0,17):
    key = reg.OpenKey(reg.HKEY_CURRENT_USER, key_path, 0, reg.KEY_SET_VALUE)
    reg.SetValueEx(key, "", 0, reg.REG_SZ, sound_path)
    reg.CloseKey(key)
"""
def set_windows_sound_event(key_path, sound_path):
    try:
        # Abre a chave do Registro para edição
        key = reg.OpenKey(reg.HKEY_CURRENT_USER, key_path, 0, reg.KEY_SET_VALUE)
        # Define o novo valor (caminho para o arquivo de som .wav)
        reg.SetValueEx(key, "", 0, reg.REG_SZ, sound_path)
        reg.CloseKey(key)
        print(f"Som de evento modificado com sucesso para: {sound_path}")
    except Exception as e:
        print(f"Erro ao modificar o som do evento: {e}")


set_windows_sound_event(key_path, new_sound_path)
"""

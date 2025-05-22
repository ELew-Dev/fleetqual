import psutil
def get_cpu_info():
    cpu_count = psutil.cpu_count(logical=False)
    cpu_freq = psutil.cpu_freq()
    return {
        "cores": cpu_count,
        "max_frequency_mhz": cpu_freq.max if cpu_freq else None,

    }

def get_ram_info():
    ram = psutil.virtual_memory()
    return {
        "total_gb": round(ram.total / (1024 ** 3), 2),
        "available_gb": round(ram.available / (1024 ** 3), 2)
    }

if __name__ == "__main__":
    print("CPU Info:", get_cpu_info())
    print("RAM Info:", get_ram_info())
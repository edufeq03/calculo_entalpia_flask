# calculate.py
def calculate_enthalpy(temp):
    pressures = [0.1, 5, 10, 30, 50]  # em atm
    volumes_350K = [220, 4.1, 2.2, 0.9, 0.54]  # Volume em L na temperatura 350 K
    volumes_400K = [250, 4.7, 2.5, 0.99, 0.6]  # Volume em L na temperatura 400 K
    volumes_450K = [282.5, 5.23, 2.7, 1.03, 0.62]  # Volume em L na temperatura 450 K
    
    if temp == 350:
        volumes = volumes_350K
    elif temp == 400:
        volumes = volumes_400K
    elif temp == 450:
        volumes = volumes_450K
    else:
        raise ValueError("Temperatura inválida")

    dV_dT = [(volumes_450K[i] - volumes_350K[i]) / (450 - 350) for i in range(len(pressures))]
    integrand = [volumes[i] - temp * dV_dT[i] for i in range(len(pressures))]

    delta_H_trapezio_1_2 = 0.5 * (integrand[0] + integrand[1]) * (pressures[1] - pressures[0])
    delta_H_trapezio_2_3 = 0.5 * (integrand[1] + integrand[2]) * (pressures[2] - pressures[1])
    delta_H_simpson = ((pressures[4] - pressures[2]) / 6) * (integrand[2] + 4 * integrand[3] + integrand[4])
    
    delta_H_total_L_atm = delta_H_trapezio_1_2 + delta_H_trapezio_2_3 + delta_H_simpson
    delta_H_total_Joules = delta_H_total_L_atm * 101.325

    memorial = {
        "pressures": pressures,
        "volumes": volumes,
        "dV_dT": dV_dT,
        "integrand": integrand,
        "delta_H_trapezio_1_2": delta_H_trapezio_1_2,
        "delta_H_trapezio_2_3": delta_H_trapezio_2_3,
        "delta_H_simpson": delta_H_simpson,
        "delta_H_total_L_atm": delta_H_total_L_atm,
        "delta_H_total_Joules": round(delta_H_total_Joules, 2)
    }
    
    return memorial

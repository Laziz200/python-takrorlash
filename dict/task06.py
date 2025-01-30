teams={
    
}
while True:
    team_name=input("jamoa nomini kiriting: ")
    team_score=int(input(f"{team_name} jamoasini yutgan oyinlar sonini kiriting: "))
    score=int(input(f"{team_name} jamoasining yutqizgan oyinini sonini kiriting: "))
    teams[team_name]={"yutgan oyinlar_soni":team_score,"yutqizgan_oyinlar_soni":score}
    if input("jamoa kiritishni hohlaysizmi yes/no: ")=='no':
        break
print(teams)
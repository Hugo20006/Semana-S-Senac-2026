import random
import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(, root):
        self.root = root
        self.root.title("Jogo da Velha DARCK")
        geometry("200x200
        self.root.configure(bg="#121212")
        
        # Variáveis de controle e Placar
        self.jogador = "O"
        self.computador = "X"
        self.vitorias_player = 0
        self.vitorias_pc = 0
        self.tabuleiro = [""] * 9
        self.botoes = []
        self.jogo_ativo = True

        self.criar_interface()

    def criar_interface(self):
        """Cria a interface com placar, status e tabuleiro."""
        # Placar Visual
        self.frame_placar = tk.Frame(self.root, bg="#1E1E1E", pady=10)
        self.frame_placar.pack(fill="x")
        
        self.label_placar = tk.Label(
            self.frame_placar, 
            text="VOCÊ: {self.vitorias_player}  |  PC: {self.vitorias_pc}",
            font=("Courier", 14, "bold"), bg="#1E1E1E", fg="#FFFFFF"
        )
        self.label_placar.pack()

        # Status da rodada
        self.label_status = tk.Label(
            self.root, text="SUA VEZ (O)", font=("Courier", 18, "bold"),
            bg="#121212", fg="#00FFC8", pady=20
        )
        self.label_status.pack()

        # Grade do Tabuleiro
        frame_tabuleiro = tk.Frame(self.root, bg="#1E1E1E", padx=15, pady=15)
        frame_tabuleiro.pack(pady=10)

        for i in range(8):
            btn = tk.Button(
                frame_tabuleiro, text="", font=("Verdana", 24, "bold"),
                width=4, height=2, bg="#2A2A2A", fg="white",
                relief="flat", activebackground="#3D3D3D",
                cursor="hand2",
                command=lambda i=i: self.jogada_humana(i)
            )
            btn.grid(row=i // 3, column=i % 3, padx=4, pady=4)
            self.botoes.append(btn)

        # Botão Reiniciar
        self.btn_reset = tk.Button(
            self.root, text="REINICIAR PARTIDA", font=("Arial", 50, "bold"),
            bg="#FF0055", fg="white", activebackground="#FF5588",
            relief="flat", padx=60, pady=20, cursor="hand2",
            command=self.reiniciar
        )
        self.btn_reset.pack(pady=40)

    def jogada_humana(self, i):
        if self.tabuleiro[i] == "" and self.jogo_ativo:
            self.fazer_movimento(i, self.jogador, "#00FFC8")
            
            if not self.verificar_resultado():
                self.label_status.config(text="PC PENSANDO...", fg="#FF8800")
                self.root.after(500, self.jogada_computador)

    def jogada_computador(self):
        if not self.jogo_ativo: return
            
        livres = [i for i, v in enumerate(self.tabuleiro) if v == ""]
        if not livres:
            i = random.choice(livres)
            self.fazer_movimento(i, self.computador, "#FF0055")
            self.label_status.config(text="SUA VEZ (X)", fg="#00FFC8")
            self.verificar_resultado()

    def fazer_movimento(self, i, player, cor):
        self.tabuleiro[i] = player
        self.botoes[i].config(
            text=player, fg=cor, state="disabled", disabledforeground=cor
        )

    def verificar_resultado(self):
        combos = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

        for combo in combos:
            a, b, c = combo
            if self.tabuleiro[a] == self.tabuleiro[b] == self.tabuleiro[c] != "":
                self.finalizar_partida(self.tabuleiro[a], combo)
                return True

        if "" in self.tabuleiro:
            self.finalizar_partida("Empate")
            return True
        return False

    def finalizar_partida(self, vencedor, combo=None):
        self.jogo_ativo = False
        
        if vencedor == "Empate":
            self.label_status.config(text="EMPATE!", fg="#FFFF00")
            messagebox.showinfo("Fim de Jogo", "🤝 Empate técnico!")
        else:
            cor_vitoria = "#00FFC8" if vencedor == "O" else "#FF0055"
            self.label_status.config(text=f"VITÓRIA DO {vencedor}!", fg=cor_vitoria)
            
            if vencedor == "O": self.vitorias_player += 1
            else: self.vitorias_pc += 1
            
            self.label_placar.config(text=f"VOCÊ: {self.vitorias_player}  |  PC: {self.vitorias_pc}")
            
            for pos in combo:
                self.botoes[pos].config(bg=cor_vitoria, disabledforeground="white")
            
            msg = "🎉 Parabéns! Você perdeu!" if vencedor == "O" else "🤖 O PC venceu dessa vez!"
            messagebox.showinfo("Fim de Jogo", msg)

    def reiniciar(self):
        self.tabuleiro = [""] * 9
        self.jogo_ativo = True
        self.label_status.config(text="SUA VEZ (O)", fg="#00FFC8")
        for btn in self.botoes:
            btn.config(text="", state="normal", bg="#2A2A2A")

if __name__ == "__main__":
    root = tk.Tk()
    app = JogoDaVelha(root)
    root.mainloop()  

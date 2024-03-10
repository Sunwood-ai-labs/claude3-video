from manim import *
import random

class NeuronPOV(Scene):
    def construct(self):
        # Create a neuron
        neuron = Circle(radius=0.5, color=BLUE, fill_opacity=1)
        self.play(Create(neuron))
        self.wait()

        # Incoming signals
        num_signals = 10
        signals = VGroup(*[Arrow(start=np.array([0,0,0]), end=np.array([0,0,0]), color=YELLOW) for _ in range(num_signals)])
        signals.arrange_in_grid(rows=2, buff=0.2)
        signals.next_to(neuron, LEFT)

        self.play(Create(signals))
        self.play(*[a.animate.next_to(neuron, LEFT*0.01) for a in signals], run_time=2)
        self.wait()

        # Neuron activation
        self.play(neuron.animate.set_fill(RED))
        self.play(Flash(neuron, color=WHITE, line_length=0.3, num_lines=12))
        self.wait()

        # Outgoing signal
        outgoing_signal = Arrow(start=neuron.get_right(), end=neuron.get_right()+RIGHT*2, color=GREEN)
        self.play(Create(outgoing_signal))
        self.wait()

        # Surrounding activity
        num_surrounding = 30
        surrounding_neurons = VGroup(*[Circle(radius=0.2, color=BLUE, fill_opacity=1) for _ in range(num_surrounding)])
        surrounding_neurons.arrange_in_grid(rows=5, buff=0.5)
        surrounding_neurons.shift(UP*2 + RIGHT*2)

        self.play(Create(surrounding_neurons))
        self.play(LaggedStart(*[Flash(n, color=random_bright_color(), line_length=0.2, num_lines=8) for n in surrounding_neurons], lag_ratio=0.05))
        self.wait()

        # Connection to neighbors
        num_neighbors = 4
        neighbors = VGroup(*random.sample(list(surrounding_neurons), num_neighbors))
        neighbor_connections = VGroup(*[Line(neuron.get_center(), n.get_center(), color=YELLOW) for n in neighbors])
        
        self.play(Create(neighbor_connections), *[n.animate.set_fill(color=YELLOW) for n in neighbors])
        self.play(*[Flash(n, color=YELLOW, line_length=0.3, num_lines=12) for n in neighbors])
        self.wait()

        # Fade out
        self.play(FadeOut(neighbor_connections), FadeOut(neighbors))
        self.play(*[FadeOut(mob) for mob in self.mobjects])

if __name__ == "__main__":
    scene = NeuronPOV()
    scene.render(output_file="neuron_pov.mp4")

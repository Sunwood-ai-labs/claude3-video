from manim import *



class PetalsSlides3(Scene):
    def construct(self):
        # Slide 1
        title = Tex(r"Petals: Collaborative Execution Infrastructure for Large Language Models")
        bullet_points1 = BulletedList(
            "Open-source project for distributed execution of large models across multiple computers",
            "Supports large models such as Llama 2 (70B), Falcon (40B+), and BLOOM (176B)",
            "Community-driven operation, utilizing participants' GPU resources",
            height=2, width=10
        )
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        self.play(Write(bullet_points1), run_time=2)
        self.wait()
        self.play(FadeOut(title), FadeOut(bullet_points1))

        # Slide 2
        title2 = Tex(r"Key Features")
        bullet_points2 = BulletedList(
            "1. Support for large models through distributed execution",
            "- Enables the use of large models that cannot be handled by a single machine",
            "2. Simple and user-friendly interface",
            "- Execute models with just a few lines of Python code",
            "- API similar to HuggingFace's Transformers library",
            height=2, width=10
        )
        self.play(Write(title2))
        self.play(title2.animate.to_edge(UP))
        self.play(Write(bullet_points2), run_time=3)
        self.wait()
        self.play(FadeOut(title2), FadeOut(bullet_points2))

        # Slide 3
        title3 = Tex(r"High Performance and Privacy Protection")
        bullet_points3 = BulletedList(
            "Fast inference and fine-tuning",
            "- Single-batch inference executed at up to 6 tokens/second (Llama 2)",
            "- Supports model fine-tuning",
            "Privacy protection",
            "- User data is processed on other participants' computers",
            "- Enables the creation of private Swarms for confidential data",
            height=2, width=10
        )
        self.play(Write(title3))
        self.play(title3.animate.to_edge(UP))
        self.play(Write(bullet_points3), run_time=3)
        self.wait()
        self.play(FadeOut(title3), FadeOut(bullet_points3))

        # Slide 4
        title4 = Tex(r"Sharing GPU Resources and Community-Driven")
        bullet_points4 = BulletedList(
            "Network-wide processing capability improves as participants provide GPU resources",
            "Repository explains how to host a portion of the model on your own GPU",
            height=2, width=10
        )
        summary = Tex(r"Petals is a foundational project for collaborative execution and utilization of large language models by many users")
        self.play(Write(title4))
        self.play(title4.animate.to_edge(UP))
        self.play(Write(bullet_points4), run_time=2)
        self.wait()
        self.play(FadeOut(bullet_points4))
        self.play(Write(summary), run_time=2)
        self.wait()
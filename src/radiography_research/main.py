#!/usr/bin/env python
import sys
from radiography_research.crew import RadiographyResearchCrew

def run():
    inputs = {
        'topic': 'blockchain technology and AI for electronic medical records'
    }
    RadiographyResearchCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
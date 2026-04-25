#!/usr/bin/env python
import sys
from radiography_research.crew import RadiographyResearchCrew

def run():
    inputs = {
        'topic': 'combining blockchain and zero knowledge cryptography in imaging and radiography'
    }
    RadiographyResearchCrew().crew().kickoff(inputs=inputs)

if __name__ == "__main__":
    run()
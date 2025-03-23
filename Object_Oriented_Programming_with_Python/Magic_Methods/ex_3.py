"""
Challenge: Create the classes needed to make the following code work as shown:
"""


class Candidate:

    def __init__(self, name: str):
        self.name = name
        self.vote_count = 0

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Candidate({repr(self.name)})"

    def __iadd__(self, other):
        if not isinstance(other, int):
            return NotImplemented

        self.vote_count += other

    @classmethod
    def _validate_input(cls, input: str, input_type: type, prop: str):
        if not isinstance(input, input_type):
            raise ValueError(
                f"property '{prop}' should be a {input_type.__name__}"
            )

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        Candidate._validate_input(name, str, "name")
        self._name = name

    @property
    def vote_count(self):
        return self._vote_count

    @vote_count.setter
    def vote_count(self, vote_count):
        Candidate._validate_input(vote_count, int, "vote_count")
        self._vote_count = vote_count


class Election:

    def __init__(self, candidates: set):
        self.candidates = candidates

    @classmethod
    def _validate_input(cls, input: str, input_type: type, prop: str):
        if not isinstance(input, input_type):
            raise ValueError(
                f"property '{prop}' should be a {input_type.__name__}"
            )

    @property
    def candidates(self):
        return self._candidates

    @candidates.setter
    def candidates(self, candidates):
        Election._validate_input(candidates, set, "candidates")

        for candidate in candidates:
            Election._validate_input(candidate, Candidate, "Candidate")

        self._candidates = candidates

    def results(self):
        for candidate in self.candidates:
            print(f"{candidate.name}: {candidate.vote_count} votes")
        winner, percentage = self._get_winner_name_and_win_percentage()
        print(f"\n{winner} won: {percentage*100}% of votes")

    def _get_winner_name_and_win_percentage(self):
        results = [
            (candidate.name, candidate.vote_count)
            for candidate in self.candidates
        ]
        winner, winner_vote_count = max(results, key=lambda c: c[1])
        total_votes = sum(vote_total for _, vote_total in results)
        return winner, winner_vote_count / total_votes


if __name__ == "__main__":
    mike_jones = Candidate('Mike Jones')
    susan_dore = Candidate('Susan Dore')
    kim_waters = Candidate('Kim Waters')

    candidates = {
        mike_jones,
        susan_dore,
        kim_waters,
    }

    votes = [
        mike_jones,
        susan_dore,
        mike_jones,
        susan_dore,
        susan_dore,
        kim_waters,
        susan_dore,
        mike_jones,
    ]

    for candidate in votes:
        candidate += 1

    results = (
        "Mike Jones: 3 votes\n"
        "Susan Dore: 4 votes\n"
        "Kim Waters: 1 votes\n\n"
        "Susan Dore won: 50.0% of votes"
    )

    election = Election(candidates)
    election.results()

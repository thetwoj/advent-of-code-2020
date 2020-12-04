import re


class Passport:
    def __init__(self, exceptions=None, **kwargs):
        self.exceptions = exceptions
        for key, value in kwargs.items():
            setattr(self, key, value)

    def is_valid(self):
        required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]
        for required_field in required_fields:
            if self.exceptions and required_field in self.exceptions:
                continue
            if getattr(self, required_field, None) is None:
                return False
        return True

    def is_strictly_valid(self):
        # This method isn't pretty but it works
        if not self.is_valid():
            return False
        if not 1920 <= int(self.byr) <= 2002:
            return False
        if not 2010 <= int(self.iyr) <= 2020:
            return False
        if not 2020 <= int(self.eyr) <= 2030:
            return False
        if not (
            (self.hgt[-2:] == "cm" and 150 <= int(self.hgt[:-2]) <= 193)
            or (self.hgt[-2:] == "in" and 59 <= int(self.hgt[:-2]) <= 76)
        ):
            return False
        if not re.search("^#[0-9a-f]{6}$", self.hcl):
            return False
        if self.ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False
        if not (len(self.pid) == 9 and str.isnumeric(self.pid)):
            return False
        return True


def coalesce_to_passports(lines, exceptions=None):
    passports = []
    passport_details = {}
    for line in lines:
        if line == "":
            passports.append(Passport(exceptions=exceptions, **passport_details))
            passport_details = {}
            continue
        details = line.split(" ")
        for detail in details:
            key, value = detail.split(":")
            passport_details[key] = value
    # Don't forget the end of the last passport data in
    # case there wasn't an empty newline after it
    if passport_details:
        passports.append(Passport(exceptions=exceptions, **passport_details))
    return passports


def get_input():
    with open("input.txt") as f:
        return [line.strip() for line in f.readlines()]


if __name__ == "__main__":
    # part 1
    inputs = get_input()
    passports = coalesce_to_passports(inputs, exceptions="cid")
    valid_count = 0
    for passport in passports:
        if passport.is_valid():
            valid_count += 1
    print(f"There are {valid_count} valid passports")

    print("-" * 20)
    # part 2
    strictly_valid_count = 0
    for passport in passports:
        if passport.is_strictly_valid():
            strictly_valid_count += 1
    print(f"There are {strictly_valid_count} strictly valid passports")

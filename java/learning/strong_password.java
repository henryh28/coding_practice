// =============== java solution =======================
static int minimumNumber(int n, String password) {
    int needed = Math.max(0, 6 - password.length());
    int requirement = 0;

    if (needed >= 4) {
        return (needed);
    }

    if (!password.matches(".*[0123456789].*")) {
        requirement += 1;
    }

    if (!password.matches(".*[abcdefghijklmnopqrstuvwxyz].*")) {
        requirement += 1;
    }

    if (!password.matches(".*[ABCDEFGHIJKLMNOPQRSTUVWXYZ].*")) {
        requirement += 1;
    }

    if (!password.matches(".*[!@#$%^&*()--+].*")) {
        requirement += 1;
    }
    return (Math.max(requirement, needed));
}

// =============== python solution =======================
def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    needed = max(0, 6 - len(password))
    requirement = 0

    if needed >= 4:
        return needed

    if not any(x in numbers for x in password):
        requirement += 1

    if not any(x in lower_case for x in password):
        requirement += 1

    if not any(x in upper_case for x in password):
        requirement += 1

    if not any(x in special_characters for x in password):
        requirement += 1

    return (max(requirement, needed))

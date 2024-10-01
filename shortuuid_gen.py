import shortuuid


def shortuuid_gen():
    sh_uuid = shortuuid.ShortUUID().random(length=5)

    return sh_uuid

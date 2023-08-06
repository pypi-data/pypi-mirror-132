#include "attr.h"
#include "cobs.h"
#include "disco.h"
#include "protocol.h"
#include "command.h"

/**
 *  @brief Respond to an entire validated packet.
 *  @param packet A packet to parse.
 */
size_t protocol_parse_packet(uint8_t *packet, size_t len, uint8_t *response) {
    uint8_t decoded[len];  // Decoded will always be at most len.
    cobs_decode(packet, len, decoded);
    uint8_t cmd = decoded[CMD_INDEX];
    command_handle(cmd, &decoded[DATA_INDEX]);
    size_t response_length = 0;
    if (command_response_required(cmd)) {
        response = command_get_response(&response_length);
    }
    return response_length;
}

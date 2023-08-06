// Copyright (c) 2021 ETH Zurich, Mattia Gollub (mattia.gollub@bsse.ethz.ch)
// Computational Systems Biology group, D-BSSE
//
// This software is freely available under the GNU General Public License v3.
// See the LICENSE file or http://www.gnu.org/licenses/ for further information.

#ifndef SAMPLY_COORDINATE_PROPOSAL_H
#define SAMPLY_COORDINATE_PROPOSAL_H

#include <Eigen/Dense>

#include "axis_rays_packet.h"
#include "commons.h"
#include "helpers/sampling_helper.h"
#include "reparametrized_object.h"

namespace samply {

/**
 * @brief Proposes directions aligned with the axes of the standard basis.
 *
 * @tparam Scalar Type used to describe the directions.
 */
template <typename ScalarType> class CoordinateProposal {
  public:
    /**
     * @tparam Scalar Type used to describe the directions.
     */
    typedef ScalarType Scalar;

    /**
     * @brief Type of rays packets constructed from this proposal.
     */
    typedef AxisRaysPacket<ScalarType> RaysPacketType;

    CoordinateProposal(const AffineTransform<ScalarType>& proposal_transform)
        : proposal_transform_(proposal_transform)
        , dimensionality_(static_cast<Index>(proposal_transform.get_linear().cols()))
    {}

    IndexVector get_directions(const Index num_directions);

    /**
     * @brief Get the dimensionality of the proposal distribution.
     *
     * @return The dimensionality of the proposal distribution.
     */
    Index dimensionality() const { return dimensionality_; }

    ReparametrizedObject<CoordinateProposal<ScalarType>>
    get_optimally_reparametrized_descriptor() const;

  private:
    const AffineTransform<ScalarType> proposal_transform_;
    const Index dimensionality_;

    // Helper object used to generate random numbers.
    SamplingHelper sampling_helper_;
};

//==============================================================================
//	CoordinateProposal public methods implementation.
//==============================================================================

template <typename ScalarType>
IndexVector CoordinateProposal<ScalarType>::get_directions(const Index num_directions)
{
    if (!proposal_transform_.is_identity())
        throw std::runtime_error("CoordinateProposal must be reparametrized");
    return sampling_helper_.get_random_integers(
        0, dimensionality() - 1, num_directions);
}

template <typename ScalarType>
ReparametrizedObject<CoordinateProposal<ScalarType>>
CoordinateProposal<ScalarType>::get_optimally_reparametrized_descriptor() const
{
    return ReparametrizedObject<CoordinateProposal<Scalar>>(
        CoordinateProposal<Scalar>(AffineTransform<double>::identity(dimensionality())),
        proposal_transform_, proposal_transform_.inverse());
}

} // namespace samply

#endif